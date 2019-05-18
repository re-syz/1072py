import math

import csv
n1 = input()
file = "./" + n1


with open(file, 'r') as csvFile:
    rows = csv.reader(csvFile)
    fil = []
    for i in rows:
        fil.append(i)

# print(fil)

fil.pop(0)

for li in fil:
    li[0] = int(li[0])
    li[1] = int(li[1])

for i in range(len(fil)):
    fil[i][1] = int(math.sqrt(fil[i][1]) * 11)

    if fil[i][1] > 100:
        fil[i][1] = 100

# print(fil)

total = 0

for li in fil:
    total += li[1]

total = total / len(fil)

print("%.1f" % total)
