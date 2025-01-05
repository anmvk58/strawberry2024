
def make_for_one_ship(str):
    str = str.lower()
    str = str.replace(":", "2.")
    str = str.replace("/", ",")
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
        {'Khải': '4007 / 4040 / 4039 / 4000 / 4026 / 4047 / 4055 / 4053 / 4049 / 4071 / 4137 / 4130 / 4136 / 4132 / 4135 /4134'},
        {'Chiến ': '4029 / 4033 / 4019 / 4023 / 4012 / 4001 / 4034 / 4054 / 3998 / 4030 / 4104 / 4105 / 4102.không một chuyển khoản / 4084 / 4073 / 4090 / 4093 / 4107 / 4108'},
        {'Nghĩa': '4094 / 4092 / 4065 / 4041 / 4068 / 4085 / 4083 / 4069 / 4013 / 4078 / 4131 / 4110'},
        {'Tâm': ''},
        {'Long': '4050 chuyển khoản / 4048 / 4056 / 4037.không một / 4021 / 4024 / 4046 / 4025/ 4052 / 4051 / 4020'},
        {'ChiếnBS': '4075 / 4100 / 4097 / 4088 / 4080 chuyển khoản / 4074 / 4072 / 4096 / 4018 / 4062'},
        {'Phong': '4003 / 4045 / 4060 / 4058 / 4004 / 4063 / 4061 / 4126 / 4125 / 4122'},
        {'Bảo': '4009 / 4032 / 4022 / 4017 / 4015 / 3992 / 3993 / 4031 / 4016 / 4008 / 4129.không một / 4128 / 4121 / 4123 / 4035 / 4111 /4109 / 4120 / 4124 / 4114'},
        {'Diện': '4036 / 4014 / 3986 / 3987 / 3991 chuyển khoản / 3990 / 3999 / 3996 / 4028 / 4042 / 4103 / 4113 / 4115 / 4118 / 4112'},
        {'Trung': '4086 / 4005 chuyển khoản / 4082 / 4091 / 4089 / 4070 / 4076 / 3994 / 4067 / 4077'},
        {'Đạt': '4079 / 4057 / 4087 / 4081 / 4066 / 4064 / 4098 / 4101/ 4038.không một'},
        {'Bắc': '4002 / 3995 / 4027 / 4006 / 3997 / 3989 chuyển khoản / 4043 / 4010 / 4011 / 3988 / 4095 / 4106 / 4116'},
        {'KhachLe': ''},
    ]

    for item in list_data:
        shipper = list(item.keys())[0]
        value = list(item.values())[0]
        if item.get(shipper) == '':
            continue
        print('{}\n{}\n'.format(shipper, make_for_one_ship(value)))



    # print(result)
    # clipboard.copy(result)




