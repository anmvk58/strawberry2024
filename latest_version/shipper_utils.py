import pandas as pd
from config import SHIP_PRICE, BASE_PATH
from latest_version.bill_utils import clean, make_bill
import dataframe_image as dfi


def calculate_for_one_ship(df, shipper_name):
    df_not_ck = df.loc[df['CK'] != 'C']
    tong_tien = sum(df_not_ck['Khách cần trả'])
    tong_don = df.shape[0]
    tien_ship = tong_don * SHIP_PRICE
    phai_thu = tong_tien - tien_ship

    data = [
        ['Tổng tiền', tong_tien],
        ['Tổng đơn', tong_don],
        ['Tiền ship', tien_ship],
        ['Cắt ship', 0],
        ['Phải thu', phai_thu],
        ['CK', None],
        ['CK', None],
        ['CK', None],
        ['CK', None],
        ['TM', None],
        ['TM', None],
        ['Tổng nộp', None],
        ['Tổng ship', None],
        ['Lệch', None],
    ]
    df_result = pd.DataFrame(data, columns=['Shipper', shipper_name])
    return df_result, tong_tien, tien_ship, phai_thu


def make_shipper(file_path):
    file_ship = open(file_path, mode="r", encoding="utf-8")
    lines = file_ship.readlines()
    list_ship = []
    new_lines = list(filter(lambda line: line != '\n', lines))

    for x in range(0, len(new_lines) - 1, 2):
        list_ship.append({new_lines[x].replace("\n", ""): new_lines[x + 1].replace("\n", "")})

    df = pd.DataFrame(columns=['Code', 'Shipper', 'CK'])
    i = 0
    for s in list_ship:
        shiper = list(s.keys())[0]
        list_bill = clean(s.get(shiper)).split("*")
        if list_bill[0] == "":
            continue
        for bill in list_bill:
            if "/" in bill:
                df.loc[i] = [make_bill(bill).replace('/', ''), shiper, 'C']
            else:
                df.loc[i] = [make_bill(bill), shiper, '']
            i += 1
    # print("ok")
    # check df trùng:
    if df['Code'].duplicated().any() == True:
        print(df[df.duplicated(['Code'], keep=False)])
        raise "Error Duplicate !!!"

    df['Shipper_code'] = df['Code']

    return df


def export_png_for_one_ship(df_ship, tong_tien, tien_ship, phai_thu, filename, shipper):
    """
    Hàm để export thông tin tính toán của 1 ship ra ảnh png, gửi vào Zalo cho nhanh
    :param df_ship: danh sách các hóa đơn chỉ của shipper đó, lọc dựa vào df_total
    :param tong_tien: Tổng tiền mà shipper thu hộ
    :param tien_ship: Tổng tiền ship của shipper
    :param phai_thu: Tổng phải thu về từ ship
    :param filename: folder lưu (yyyymmdd)
    :param shipper: tên shipper  (lấy trong vòng lặp)
    """
    # create cục dữ liệu summary bên dưới data của 1 ship
    list_columns = ['Mã hóa đơn', 'Khách hàng', 'Điện thoại', 'Địa chỉ (Khách hàng)', 'Shipper', 'CK', 'Khách cần trả',
                    'Total money']
    sum_data_ship = [
        ['', '', '', '', '', 'Tổng tiền', tong_tien, ''],
        ['', '', '', '', '', 'Tiền ship', tien_ship, ''],
        ['', '', '', '', '', 'Phải thu', phai_thu, '']
    ]
    temp_df = pd.DataFrame(data=sum_data_ship,
                           columns=list_columns)

    df_ship_to_png = df_ship[list_columns]

    df_ship_to_png = pd.concat([df_ship_to_png, temp_df], ignore_index=True)
    dfi.export(df_ship_to_png, "{}\\{}\\{}.png".format(BASE_PATH, filename, shipper), dpi=150)
