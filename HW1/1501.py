"""
131072
170318
107-2 Python HW1
1501



"""


# =============

n = str(input())

sol = 0  # default 0 = NO, 1 = YES

n_list = []

for i in n:
    n_list.append(i)

# print (n_list)

for i in n_list:
    if int(i) == 7:
        sol = 1

n = int(n)

if n % 7 == 0:
    sol = 1

if sol == 1:
    print("YES")

else:
    print("NO")
