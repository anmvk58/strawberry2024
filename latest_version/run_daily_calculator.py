import os
import time

import pandas as pd
import numpy as np
from datetime import datetime

from latest_version.bill_utils import format_sheet_excel, additional_info_for_total_ship, format_sheet_excel_total_ship
from latest_version.config import BASE_PATH, SHIP_PATH, KIOT_PATH, KIOT_PATH2
from latest_version.shipper_utils import make_shipper, calculate_for_one_ship, export_png_for_one_ship

if __name__ == '__main__':
    # filename = datetime.today().strftime('%Y%m%d')
    # filename = "20250126"
    filename = input("Enter rundate (YYYYMMDD): \n")

    # Đọc dữ liệu thống kê shipper đi đơn
    df_shipper = make_shipper(SHIP_PATH)

    # Đọc dữ liệu bán hàng xuất từ kiot việt
    df_kiotviet = pd.read_excel(KIOT_PATH.format(BASE_PATH, filename))

    # df_kiotviet1 = pd.read_excel(KIOT_PATH.format(BASE_PATH, filename))
    # df_kiotviet2 = pd.read_excel(KIOT_PATH2.format(BASE_PATH, filename))
    #
    # df_kiotviet = pd.concat([df_kiotviet1, df_kiotviet2], ignore_index=True)

    # ******** Kiểm tra nếu số lượng đơn không khớp và báo
    if df_kiotviet.shape[0] > df_shipper.shape[0]:
        print("--- Check: Phần mềm nhiều hơn Shipper !!!")
    elif df_kiotviet.shape[0] < df_shipper.shape[0]:
        print("--- Check: Shipper nhiều hơn phần mềm !!!")
    else:
        print("--- Check: Ship và Phần mềm Khớp !!!")

    df_total = pd.merge(df_kiotviet, df_shipper, left_on=['Mã hóa đơn'], right_on=['Code'], how="outer")

    # Lấy danh sách các shipper
    list_shipper = df_shipper['Shipper'].unique()

    # Bổ sung thêm cột mới là [Total money] copy từ cột [Khách cần trả]
    df_total['Total money'] = df_total.loc[:, 'Khách cần trả']

    # Reorder column
    df_total = df_total[
        ['Mã hóa đơn', 'Khách hàng', 'Điện thoại', 'Địa chỉ (Khách hàng)', 'Shipper', 'CK', 'Khách cần trả',
         'Total money', 'Shipper_code']]

    # Tìm những đơn chuyển khoản và gán giá trị cột [Khách cần trả] = 0
    df_total["Khách cần trả"] = np.where(df_total["CK"] == "C", 0, df_total["Khách cần trả"])

    # Khởi tạo df rỗng để lưu kết quả tính summary của shipper
    total_shipper_df = pd.DataFrame()

    # Start Export kết quả ra xlsx và export ra ảnh tính của từng ship
    try:
        # os.mkdir(f"{BASE_PATH}\\{filename}")
        writer = pd.ExcelWriter(f"{BASE_PATH}\\{filename}_result.xlsx", engine='xlsxwriter')
        df_total.to_excel(writer, sheet_name='Invoices', index=False)
    except Exception as e:
        print(f"Thư mục [{filename}] đã tồn tại")
        cmd = input(f"Nhập y để tiếp tục chạy: \n")
        if cmd == 'y' or cmd == 'Y':
            writer = pd.ExcelWriter(f"{BASE_PATH}\\{filename}_result.xlsx", engine='xlsxwriter')
            df_total.to_excel(writer, sheet_name='Invoices', index=False)
        else:
            raise Exception("Chạy lại chú ý !!!")
    finally:
        # thực hiện format cho đẹp:
        format_sheet_excel(writer, 'Invoices')
        print("Ghi kết quả tổng hợp thành công ! \n")

    # Start tính cho từng shipper:
    for ship in list_shipper:
        df_ship = df_total.loc[df_total['Shipper'] == ship]
        df_cal_one_ship, tong_tien, tien_ship, phai_thu = calculate_for_one_ship(df_ship, ship)
        total_shipper_df = pd.concat([total_shipper_df, df_cal_one_ship], axis=1)

        # ghi vào 1 sheet riêng total và details của 1 ship
        df_cal_one_ship.head(5).to_excel(writer, sheet_name=ship, index=False, startrow=0, startcol=0)
        df_ship.to_excel(writer, sheet_name=ship, index=False, startrow=7, startcol=0)

        # format định dạng độ dài các cột trong sheet của ship để dễ nhìn:
        format_sheet_excel(writer, ship)

        # export ra ảnh tính toán của 01 ship để gửi qua zalo cho tiện
        # export_png_for_one_ship(df_ship, tong_tien, tien_ship, phai_thu, filename, ship)
        # time.sleep(0.2)
        print("--- Done: {}".format(ship))

    # ghi kết quả tổng hợp các shipper vào cuối của trang tính:
    total_shipper_df.to_excel(writer, sheet_name="Total", index=False, startrow=2, startcol=0)

    # bổ sung các trường thông tin để check Ship tự động.
    additional_info_for_total_ship(writer=writer, sheet_name="Total", numb_of_shipper=len(list_shipper))

    # format lại kiểu số để dễ nhập
    format_sheet_excel_total_ship(writer=writer, sheet_name="Total", number_of_col=len(list_shipper))

    writer.close()

    print('Finish ' + filename)


