from latest_version.config import CAL_PATH

if __name__ == '__main__':
    f = open(CAL_PATH, mode="r", encoding="utf-8")
    lines = f.readlines()

    list_sl = []

    for line in lines:
        line = line.replace("\"", "")
        line = line.replace("cb bi nhỡ", "combo_bi_nho")
        line = line.replace("cb 4 bi", "combo_4_bi")
        line = line.replace("cb bi", "combo_bi")
        line = line.replace("cb vip nhỡ", "combo_vip_nho")
        line = line.replace("cb vip bi", "combo_vip_bi")
        line = line.replace("cb nhỡ bi", "combo_nho_bi")
        line = line.replace("cb nhỡ", "combo_nho")
        temp = line.replace("\"", "").replace("hộp quà ", "").replace("  ", " ").split(" ")
        obj_temp = [temp[1].replace("\n", "").lower(), temp[0]]
        list_sl.append(obj_temp)
        # print(obj_temp)

    svip = 0
    vip = 0
    nho = 0
    bi = 0
    ve = 0
    combo_bi_nho = 0
    combo_bi = 0
    combo_vip_nho = 0
    combo_vip_bi = 0
    combo_nho = 0
    combo_nho_bi = 0
    combo_4_bi = 0
    quyt = 0

    for obj in list_sl:
        if obj[0].lower() == "svip":
            svip += float(obj[1])
        if obj[0].lower() == "vip":
            vip += float(obj[1])
        if obj[0].lower() == "nhỡ":
            nho += float(obj[1])
        if obj[0].lower() == "bi":
            bi += float(obj[1])
        if obj[0].lower() == "ve":
            ve += float(obj[1])
        if obj[0].lower() == "combo_bi_nho":
            combo_bi_nho += float(obj[1])
        if obj[0].lower() == "combo_bi":
            combo_bi += float(obj[1])
        if obj[0].lower() == "combo_vip_nho":
            combo_vip_nho += float(obj[1])
        if obj[0].lower() == "combo_nho":
            combo_nho += float(obj[1])
        if obj[0].lower() == "combo_vip_bi":
            combo_vip_bi += float(obj[1])
        if obj[0].lower() == "combo_nho_bi":
            combo_nho_bi += float(obj[1])
        if obj[0].lower() == "combo_4_bi":
            combo_4_bi += float(obj[1])
        if obj[0].lower() == "quýt":
            quyt += float(obj[1])

    print("Svip: " + str(svip))
    print("Vip: " + str(vip + combo_vip_nho / 2 + combo_vip_bi))
    print("Nhỡ: " + str(nho + combo_bi_nho / 2 + combo_vip_nho / 2 + combo_nho * 2 + combo_nho_bi))
    print("Bi: " + str(bi + combo_bi_nho / 2 + combo_bi * 1.5 + combo_vip_bi + combo_nho_bi + combo_4_bi * 2))
    print("Ve: " + str(ve))
    print("Quýt: " + str(quyt))
    # print("Combo bi nhỡ: " + str(combo_bi_nho))
    # print("Combo bi: " + str(combo_bi))
    print("Total: " + str(
        svip + vip + nho + bi + ve + combo_bi_nho + combo_vip_nho + combo_vip_bi * 2 + combo_nho_bi * 2 + combo_bi * 1.5 + combo_nho * 2 + combo_4_bi * 2))
