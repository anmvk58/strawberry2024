
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
        {'Nam': '326,2 96,3 05,3 02,3 18,3 35,3 40,3 20,3 57,3 23,3 56,3 16,3 47,3 59,344 chuyển khoản'},
        {'Chiến ': '307,3 09,2 94,3 01,2 95,292.01,333 chuyển khoản, 329,3 38,3 30,3 37,3 46,350.02,3 48,3 58,339, 328,3 61,351'},
        {'Nghĩa': '343,299.01,2 98,3 12,3 34,3 03,3 06,3 22,3 42,3 55,3 52,3 27,362,353 chuyển khoản, 364'},
        {'Toàn': '297,3 31,3 32,3 10,3 36,3 15,3 13,300,3 04,3 24,3 54,3 63,3 17,311,360.01,365'},
        {'Xanh39K': '366'},
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




