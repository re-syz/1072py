"""
131072
170318
107-2 Python HW1
3050



"""


# =============

n = int(input())
cur = 0

for i in range(1, n + 1):
    for ii in range(i):
        cur += 1
        if ii == i - 1:
            print(cur, end = " \n")

        else:
            print(cur, end = " ")
