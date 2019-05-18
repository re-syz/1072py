n1 = input()

nf = "./" + n1

fil = open(nf , 'r').readlines()

for i in range(len(fil)):
    if i != len(fil) - 1:
        fil[i] = fil[i].replace("\n", "")

    if " " in fil[i]:
        fil[i] = fil[i].replace(" ", "")

    if i % 2 != 0:
        fil[i] = int(fil[i])

# print(fil)

renew = []

for i in range(len(fil)):
    if i % 2 != 0:
        if fil[i] >= 50:
            renew.append([fil[i-1], fil[i]])

# print(renew)

for i in range(len(renew)):
    cur = ""
    cur = renew[i][0] + " " + str(renew[i][1])
    print(cur)
