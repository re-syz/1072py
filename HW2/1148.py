"""
131072
170419
1148
"""


# ============= #

tri_list = []
name = []
while True:
    cur = ""
    cur = input()

    if cur == "-1":
        break

    else:
        cur = cur.split(" ")
        name.append(cur[0])
        cur.pop(0)

        for i in range(len(cur)):
            cur[i] = int(cur[i])

        cur.sort()
        tri_list.append(cur)



# ============= #
type = []
for i in range(4):
    type.append([])

for i in range(len(tri_list)):
    if tri_list[i][0] + tri_list[i][1] <= tri_list[i][2] or tri_list[i][0] + tri_list[i][2] <= tri_list[i][1] or tri_list[i][1] + tri_list[i][2] <= tri_list[i][0]:
        type[0].append(name[i])

    elif tri_list[i][0] ** 2 + tri_list[i][1] ** 2 > tri_list[i][2] ** 2:
        type[1].append(name[i])

    elif tri_list[i][0] ** 2 + tri_list[i][1] ** 2 < tri_list[i][2] ** 2:
        type[2].append(name[i])

    elif tri_list[i][0] ** 2 + tri_list[i][1] ** 2 == tri_list[i][2] ** 2:
        type[3].append(name[i])


# ============= #

for i in range(len(type)):
    if type[i] == []:
        type[i].append("None")

    type[i].sort()


pr = ["Not Triangle: ", "Acute Angle: ", "Obtuse Angle: ", "Right Angle: "]
for i in range(4):
    for ii in range(len(type[i])):
        if ii != len(type[i]) - 1:
            pr[i] += type[i][ii]
            pr[i] += ","
        else:
            pr[i] += type[i][ii]

for i in range(4):
    print(pr[i])
