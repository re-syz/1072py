import math

import csv
n1 = input()
file = "./" + n1


with open(file, 'r') as csvFile:
    rows = csv.reader(csvFile)
    fil = []
    for i in rows:
        fil.append(i)

print(fil)

fil.pop(0)
