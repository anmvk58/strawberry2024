import pandas as pd

def clean(str):
    s1 = str.replace(" ", "")
    s1 = s1.replace("năm", "5")
    s1 = s1.replace("ba", "3")
    s1 = s1.replace("lăm", "5")
    s1 = s1.replace("không", "0")
    s1 = s1.replace("một", "1")
    return s1

def make_bill(str):
    if "." in str:
        str_new = str[0:-3]
        check = True
    else:
        str_new = str
        check = False

    if len(str_new) == 4:
        if check:
            return "HD00" + str.replace("/", "")
        else:
            return "HD00" + str_new
    elif str_new.startswith('HD'):
        return str_new
    else:
        if check:
            return "HD0" + str.replace("/", "")
        else:
            return "HD0" + str_new

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

#
# if __name__ == '__main__':
#
#     # ship = [
#     #     {"Tuấn": "9921.01*9952*9940*9937*9938*9930*9949*9917.01*9935"},
#     #     {"Chiến": "9985/*9924*9976*9990*9989/*9916*9980*9923/*9966.02*9948*9920*9941*9984*9979*9975*9931*9926*9977.01*9962"},
#     #     {"Đoàn": "9922*9918*9956*9960*9981*9967*9988*9992*9993*9973*9932*9961*9965*9954*9919*9963*9946/*9982*9974.01"},
#     #     {"Thanh": "9942*9972.01*9968*9928*9953*9958*9971*9964*9951*9936"},
#     #     {"Khải": "9934*9950*9933*9970*9969*9955*9939*9944*9987*9957*9959*9991*9927*9945*9978*9986"},
#     #     {"khach le": ""}
#     # ]
#     f = open("C:\\Users\\AnMV\\Desktop\\Temp\\\Dâu\\input_ship.txt", mode="r", encoding="utf-8")
#     lines = f.readlines()
#
#     list_ship = []
#
#     new_lines = list(filter(lambda line: line != '\n', lines))
#
#     for x in range(0, len(new_lines) - 1, 2):
#         list_ship.append({new_lines[x].replace("\n", ""): new_lines[x + 1].replace("\n", "")})
#
#
#     df = pd.DataFrame(columns=['Code', 'Shipper', 'CK'])
#     i = 0
#     for s in list_ship:
#         shiper = list(s.keys())[0]
#         list_bill = clean(s.get(shiper)).split("*")
#         if list_bill[0] == "":
#             continue
#         for bill in list_bill:
#             if "/" in bill:
#                 df.loc[i] = [make_bill(bill).replace('/', ''), shiper, 'C']
#             else:
#                 df.loc[i] = [make_bill(bill), shiper, '']
#             i += 1
#
#     df.to_excel("C:\\Users\\AnMV\\Desktop\\shiptoday.xlsx", index=False)
