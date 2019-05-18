year_list = []
while True:
    inp = input()
    if inp == "q":
        break
    else:
        year_list.append(int(inp))



ten = ['癸','甲','乙','丙','丁','戊','已','庚','辛','壬']
di = ['亥','子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
result = []


def YEAR(y_list):
    for i in range(len(y_list)):
        cur = y_list[i] - 3

        ten_indi = cur % 10
        di_indi = cur % 12

        ten_cur = ten[ten_indi]
        di_cur = di[di_indi]

        cur_out = str(y_list[i]) + " = " + ten_cur + di_cur + "年"

        result.append(cur_out)

    for li in result:
        print(li)

YEAR(year_list)
