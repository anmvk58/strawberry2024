def clean(string):
    result = string.replace(" ", "")
    result = result.replace("năm", "5")
    result = result.replace("ba", "3")
    result = result.replace("lăm", "5")
    result = result.replace("không", "0")
    result = result.replace("một", "1")
    return result


def generate_zero(n):
    """
    Hàm này chỉ để generate mỗi chuỗi gồm n số 0 với n được truyền vào
    :param n: số length chuỗi cần gen
    :type n: int
    :return:
    """
    result = ''
    for i in range(n):
        result += '0'
    return result


def make_bill(bill):
    """
    Chuyển đổi thành mã bill đúng với Kiot Việt. định dạng là HD000107 (length = 8)
    Đối với mã đã được update -> sẽ có thêm hậu tố .01 ví dụ HD000107.01, HD000107.02 tùy vào update bao nhiêu lần
    Đối với mã đã được chuyển khoản -> sẽ có thêm hậu tố / để đánh dấu làm bước xử lý tính toán tiền
    :param bill: mã bill được nhập từ input txt
    :type bill: str
    :return: mã bill đã được chuẩn hóa
    """
    # nếu bắt đầu = HD thì return luôn
    if bill.startswith("HD"):
        return bill

    # nếu length >= 9 thì return luôn
    if "." in bill or "/" in bill:
        if len(bill[:bill.find('.')]) >= 8:
            return bill
    else:
        if len(bill) >= 9:
            return bill

    # 1.check có phải đơn chỉnh sửa hay không:
    modify_flag = False
    if '.' in bill:
        modify_flag = True

    # 2.tính ra mã bill gốc nhập từ txt (bỏ qua đơn sửa . và đơn chuyển khoản /)
    if modify_flag:
        org_bill_code = bill[:bill.find('.')]
    else:
        org_bill_code = bill.replace('/', '')

    # 3.tính ra mã bill chuẩn với hệ thống kiotviet:
    kiot_bill = 'HD' + generate_zero(6 - len(org_bill_code)) + org_bill_code

    # 4.thêm vào hậu tố đơn sửa và đơn chuyển khoản nếu có:
    if modify_flag:
        kiot_bill += bill[bill.find('.'):bill.find('.') + 3]
    if '/' in bill:
        kiot_bill += '/'

    return kiot_bill


def format_sheet_excel(writer, sheet_name):
    worksheet = writer.sheets[sheet_name]
    workbook = writer.book
    number_format = workbook.add_format({'num_format': '#,##0'})

    worksheet.set_column(0, 0, 13)  # Mã hóa đơn
    worksheet.set_column(1, 1, 20)  # Khách hàng
    worksheet.set_column(2, 2, 12)  # Điện thoại
    worksheet.set_column(3, 3, 70)  # Địa chỉ
    worksheet.set_column(4, 4, 10)  # Shipper
    worksheet.set_column(5, 5, 5)  # CK
    worksheet.set_column(6, 6, 13, number_format)  # Khách cần trả
    worksheet.set_column(7, 7, 13, number_format)  # Total_money
    worksheet.set_column(8, 8, 13)  # Shipper_code


def additional_info_for_total_ship(writer, sheet_name, numb_of_shipper):
    """
    Hàm thêm các trường thông tin phụ để tính tiền VAR với ship
    :param writer: openxyl
    :param sheet_name: sheet muốn thực hiện sửa
    :param numb_of_shipper: số lượng shipper
    """
    worksheet = writer.sheets[sheet_name]
    for i in range(numb_of_shipper):
        # lấy kí tự chr(65) = A
        if (66 + i * 2) <= 90:
            char_i = chr(66 + i * 2)
        elif (66 + i * 2) <= 116:
            char_i = 'A' + chr(66 + i * 2 - 26)
        else:
            char_i = 'B' + chr(66 + i * 2 - 26*2)
        # print(char_i)
        # Tổng tiền nộp =SUM(B8:B13)
        # print(f"{char_i}15", "=SUM({CHAR}9:{CHAR}14)".format(CHAR=char_i))
        worksheet.write_formula(f"{char_i}15", "=SUM({CHAR}9:{CHAR}14)".format(CHAR=char_i))

        # Tổng tiền ship =B5+B6
        worksheet.write_formula(f"{char_i}16", "={CHAR}6+{CHAR}7".format(CHAR=char_i))

        # Lệch =B4-B14
        worksheet.write_formula(f"{char_i}17", "={CHAR}4-{CHAR}15".format(CHAR=char_i))

    # format width of all column
    for j in range(numb_of_shipper * 2):
        worksheet.set_column(j, j, 12)


def format_sheet_excel_total_ship(writer, sheet_name, number_of_col):
    worksheet = writer.sheets[sheet_name]
    workbook = writer.book
    number_format = workbook.add_format({'num_format': '#,##0'})

    for i in range(number_of_col):
        worksheet.set_column(i*2 + 1, i*2 + 1, 12, number_format)
