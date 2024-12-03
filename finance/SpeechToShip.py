
def make_for_one_ship(str):
    str = str.lower()
    str = str.replace("chuyển khoản", "/")
    str = str.replace(" ", "")
    str = str.replace("một", "1")
    str = str.replace("hai", "2")
    str = str.replace("ba", "3")
    str = str.replace("bốn", "4")
    str = str.replace("năm", "5")
    str = str.replace("sáu", "6")
    str = str.replace("bảy", "7")
    str = str.replace("tám", "8")
    str = str.replace("chín", "9")
    str = str.replace("không", "0")

    result = str.replace(",", "*")
    return result


if __name__ == '__main__':
    list_data = [
        {'Khải': '23520,2 3518,23527, 23510,23515, 23546.01,23513,2 3548,23 năm ba 1,23511, 23525, 23545, 23541, 23 năm ba bẩy chuyển khoản, 23516,2 3550,2 3522,23561'},
        # {'Đoàn ': ''},
        {'Tâm': '23526,2 3543,2 3514,2 3512,23521, 23544.01,2 3519,23524,23 năm ba ba.01,23554,23555, 23540,23 năm ba 2,23557 chuyển khoản, 23528,235 năm ba, 23556,23558 chuyển khoản'},
        # {'Tuấn': ''},
        # {'Chiến': '21252,2 1251,21247, 21210,21243.01,2 1214,21224.01,2 1200,2 1202,21229 chuyển khoản, 21208,21203,21177.01,21206 chuyển khoản, 21182'},
        # {'Tư': ''},
        # {'Hiếu': '21250,2 1234,21212.01,2 1233,2 1221,2 1240,2 1231,2 1230,2 1245,2 1223,2 1190,21181, 21198,211 94,2 1188,2 1168,2 1173,2 1183,21199.không một'},
        # {'Khách lẻ': ''}
    ]

    for item in list_data:
        shipper = list(item.keys())[0]
        value = list(item.values())[0]
        print('{}\n{}\n'.format(shipper, make_for_one_ship(value)))



    # print(result)
    # clipboard.copy(result)




