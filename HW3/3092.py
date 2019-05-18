n1 = input()

nf = "../app/" + n1

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
        renew.append([fil[i-1], fil[i]])

# print(renew)

total = 0
for i in range(len(renew)):
    total += renew[i][1]

avg = 0.0
avg = total / len(renew)

for i in range(len(renew)):
    cur = ""
    cur = "chef" + " " + renew[i][0] + " " + str(renew[i][1])
    print(cur)

print("Total: " + str(total))
print("Avg: %.2f" % avg )
