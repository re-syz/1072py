n1 = input()

fil = open(n1, 'r').readlines()

# print(len(fil))

for i in range(len(fil) - 1):
    fil[i] = fil[i].replace("\n", "")
# print(fil)

# pi = 0
# sm = 1
# sh = 2
# ar = 3
# sn = 4

gun = [0, 0, 0, 0, 0]

for gu in fil:
    cur = ""
    for char in gu:
        if char == "-":
            break

        else:
            cur += char

    if cur == "PISTOL":
        gun[0] += 1

    elif cur == "SMG":
        gun[1] += 1

    elif cur == "SHOTGUN":
        gun[2] += 1

    elif cur == "AR":
        gun[3] += 1

    elif cur == "SNIPER":
        gun[4] += 1


for i in range(len(gun)):
    if i == len(gun) - 1:
        print(gun[i], end = "")

    else:
        print(gun[i], end = " ")
