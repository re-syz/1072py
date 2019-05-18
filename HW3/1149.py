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

for i in range(len(fil)):
    for ii in range(1, 6):
        fil[i][ii] = int(fil[i][ii])

final = []

for i in range(len(fil)):
    exam = 0.0
    hw = 0.0

    exam = float((fil[i][1] + fil[i][2] + fil[i][3] + fil[i][4]) / 4)
    hw = float((fil[i][5] / 40) * 100)

    fin = 0
    fin = exam * 0.7 + hw * 0.3

    if fin < 60:
        if hw == 100:
            fin = 60

    final.append([fil[i][0], fin])


for i in range(len(final)):
    cur = ""

    cur = str(final[i][0]) + " " + "%.2f" % final[i][1]

    print(cur)
