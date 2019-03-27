"""
131072
170318
107-2 Python HW1
1401



"""


# =============

int_list = []
float_list = []

while True:
    inp = input()

    if inp != "q":
        inp = float(inp)
        if int(inp) == inp:
            int_list.append(int(inp))

        else:
            float_list.append(inp)

    else:
        break

cur_int = 1
cur_float = 1.00

for i in int_list:
    cur_int *= i

for i in float_list:
    cur_float *= i


print("%.2f" % cur_float)
print(int(cur_int))

if cur_int > cur_float:
    print("Float < Int")

elif cur_int == cur_float:
    print("Float = Int")

else:
    print("Float > Int")
