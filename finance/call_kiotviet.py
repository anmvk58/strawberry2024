import os
import pandas as pd
import numpy as np
import dataframe_image as dfi
from datetime import datetime
from make_df_shipper import make_shipper

filename = datetime.today().strftime('%Y%m%d')
# filename = "20240720"

BASE_PATH = "C:\\Users\\AnMV\\Desktop\\Dâu"
KIOT_PATH = "{}\\{}.xlsx".format(BASE_PATH, filename)
SHIP_PATH = "{}\\input_ship.txt".format(BASE_PATH)

SHIP_PRICE = 26000

def calculate_for_one_ship(df, shipper_name):
    df_notchuyenkhoan = df.loc[df['CK'] != 'C']
    tong_tien = sum(df_notchuyenkhoan['Khách cần trả'])
    tong_don = df.shape[0]
    tien_ship = tong_don * SHIP_PRICE
    phai_thu = tong_tien - tien_ship

    data = [['Tổng tiền', tong_tien], ['Tiền ship', tien_ship], ['Cắt ship', 0], ['Phải thu', phai_thu]]
    df_result = pd.DataFrame(data, columns=['Shipper', shipper_name])
    return df_result, tong_tien, tien_ship, phai_thu


if __name__ == '__main__':
    df_shipper = make_shipper(SHIP_PATH)

    df_kiotviet = pd.read_excel(KIOT_PATH)

    # Check df_kiot have to equals with df_shipper
    if df_kiotviet.shape[0] > df_shipper.shape[0]:
        df_total = pd.merge(df_kiotviet, df_shipper, left_on=['Mã hóa đơn'], right_on=['Code'], how="left")
        print("Phần mềm nhiều hơn Shipper !!!")
    elif df_kiotviet.shape[0] < df_shipper.shape[0]:
        df_total = pd.merge(df_kiotviet, df_shipper, left_on=['Mã hóa đơn'], right_on=['Code'], how="right")
        print("Shipper nhiều hơn phần mềm !!!")
    else:
        df_total = pd.merge(df_kiotviet, df_shipper, left_on=['Mã hóa đơn'], right_on=['Code'], how="left")
        print("Ship và Phần mềm Khớp !!!")

    list_shipper = df_shipper['Shipper'].unique()

    # Duplicate column
    df_total['Total money'] = df_total.loc[:, 'Khách cần trả']
    # Reorder column
    df_total = df_total[
        ['Mã hóa đơn', 'Khách hàng', 'Điện thoại', 'Địa chỉ (Khách hàng)', 'Shipper', 'CK', 'Khách cần trả',
         'Total money', 'Shipper_code']]

    df_total["Khách cần trả"] = np.where(df_total["CK"] == "C", 0, df_total["Khách cần trả"])

    total_shipper_df = pd.DataFrame()
    # export images
    try:
        os.mkdir(f"{BASE_PATH}\\{filename}")
        writer = pd.ExcelWriter(f"{BASE_PATH}\\{filename}_result.xlsx", engine='xlsxwriter')
        df_total.to_excel(writer, sheet_name='Invoices', index=False)
    except:
        print("Thư mục đã tồn tại")
        cmd = input(f"Nhập y để vẫn chạy: {filename}")
        if cmd == 'y' or cmd == 'Y':
            writer = pd.ExcelWriter(f"{BASE_PATH}\\{filename}_result.xlsx", engine='xlsxwriter')
            df_total.to_excel(writer, sheet_name='Invoices', index=False)
        else:
            raise Exception("Chạy lại chú ý !!!")

    for ship in list_shipper:
        df_ship = df_total.loc[df_total['Shipper'] == ship]
        df_cal, tong_tien, tien_ship, phai_thu = calculate_for_one_ship(df_ship, ship)

        total_shipper_df = pd.concat([total_shipper_df, df_cal], axis=1)

        df_ship = df_ship.astype({"Điện thoại": str})

        df_cal.to_excel(writer, sheet_name=ship, index=False, startrow=0, startcol=0)
        df_ship.to_excel(writer, sheet_name=ship, index=False, startrow=df_cal.shape[0] + 2, startcol=0)

        data = [
            ['', '', '', '', '', 'Tổng tiền', tong_tien, '', ''],
            ['', '', '', '', '', 'Tiền ship', tien_ship, '', ''],
            ['', '', '', '', '', 'Phải thu', phai_thu, '', '']
        ]

        # Create the pandas DataFrame
        temp_df = pd.DataFrame(data,
                               columns=['Mã hóa đơn', 'Khách hàng', 'Điện thoại', 'Địa chỉ (Khách hàng)', 'Shipper',
                                        'CK', 'Khách cần trả', 'Total money', 'Shipper_code'])

        # format width
        sheet = writer.sheets[ship]
        sheet.set_column(0, 0, 13)
        sheet.set_column(1, 1, 20)
        sheet.set_column(2, 2, 12)
        sheet.set_column(3, 3, 70)
        sheet.set_column(4, 4, 8)
        sheet.set_column(5, 5, 5)
        sheet.set_column(6, 6, 10)

        # ship_df = df_ship.append(temp_df, ignore_index=True)
        ship_df = pd.concat([df_ship, temp_df], ignore_index=True)
        dfi.export(ship_df, "{}\\{}\\{}.png".format(BASE_PATH, filename, ship), dpi=150)

        # print(df_cal)
        print("--- Done: {}".format(ship))

    total_shipper_df.to_excel(writer, sheet_name="Total", index=False, startrow=df_cal.shape[0] + 2, startcol=0)
    writer.close()

    # workbook = xlsxwriter.Workbook.(f"{BASE_PATH}\\{filename}_result.xlsx")
    # for ship in list_shipper:
    #     print(ship)
    #     ws = workbook.get_worksheet_by_name(ship)
    #     ws.set_column(1, 1, 25)
    #
    # workbook.close()
    print('Finish ' + filename)
