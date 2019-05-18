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

for cou in fil:
    cou[2] = int(cou[2])

cre = [0, 0]

for cou in fil:
    if cou[3] == "F":
        continue

    else:
        if cou[1] == "R":
            cre[0] += cou[2]

        elif cou[1] == "E":
            cre[1] += cou[2]


# print (cre)

# cre[0] = cre[0] - 1
# cre[1] = cre[1] - 1

status = [0, 0]

print("Required: " + str(cre[0]))
print("Elective: " + str(cre[1]))

if cre[0] < 72 or cre[1] < 28:
    print("N")

    if cre[0] < 72:
        status[0] = 1

    if cre[1] < 28:
        status[1] = 1
else:
    print("Y")

if status[0] == 1 and status[1] == 1:
    print("Student still needs to complete " + str(72 - cre[0]) + " required credits & " + str(28 - cre[1]) + " elective credits for graduation.")

elif status[0] == 1:
    print("Student still needs to complete " + str(72 - cre[0]) + " required credits for graduation.")

elif status[1] == 1:
    print("Student still needs to complete " + str(28 - cre[1]) + " elective credits for graduation.")
