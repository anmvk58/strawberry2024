if __name__ == '__main__':
    f = open("C:\\Users\\AnMV\\Desktop\\Temp\\\Dâu\\input_ship.txt", mode="r", encoding="utf-8")
    lines = f.readlines()

    list_ship = []

    new_lines = list(filter(lambda line: line != '\n', lines))

    for x in range(0, len(new_lines) - 1, 2):
        list_ship.append({new_lines[x].replace("\n", ""): new_lines[x+1].replace("\n", "")})



    print(list_ship)
