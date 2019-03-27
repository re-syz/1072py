"""
131072
170318
107-2 Python HW1
3031



"""


# =============

n = int(input())

dozen = n // 12
remain = n % 12

if remain != 0:
    print(str(dozen) + " dozen and " + str(remain))
else:
    print(str(dozen) + " dozen")
