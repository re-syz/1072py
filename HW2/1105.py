info = [[76, 73, 85], [88, 84, 76], [92, 82, 92], [82, 91, 85], [72, 74, 73]]

for i in range(5):
    sum = 0
    avg = 0

    sum = info[i][0] + info[i][1] + info[i][2]
    avg = sum / 3

    info[i].append(sum)
    info[i].append(avg)

# print(info)

for i in range(5):

    print("student " + str(i + 1))
    print(" 1: " + str(info[i][0]))
    print(" 2: " + str(info[i][1]))
    print(" 3: " + str(info[i][2]))
    print(" sum: " + str(info[i][3]))
    print(" avg: %.2f" % info[i][4])


total_sum = 0
total_avg = 0.00
highest_stu = 0
highest_avg = 0.00

for i in range(5):
    total_sum += info[i][3]
    total_avg += info[i][4]

    if info[i][4] > highest_avg:
        highest_stu = i + 1
        highest_avg = info[i][4]

total_avg = total_avg / 5

print("total: " + str(total_sum) + ", avg: %.2f" % total_avg)
print("highest avg: student " + str(highest_stu) + ": %.2f" % highest_avg)
