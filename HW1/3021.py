"""
131072
170318
107-2 Python HW1
3021



"""


# =============

sc = int(input())

if 90 <= sc <= 100:
    print(float(4.3))
    print("A+")

elif 85 <= sc <= 89:
    print(float(4.0))
    print("A")

elif 80 <= sc <= 84:
    print(float(3.7))
    print("A-")

elif 77 <= sc <= 79:
    print(float(3.3))
    print("B+")

elif 73 <= sc <= 76:
    print(float(3.0))
    print("B")

elif 70 <= sc <= 72:
    print(float(2.7))
    print("B-")

elif 67 <= sc <= 69:
    print(float(2.3))
    print("C+")

elif 63 <= sc <= 66:
    print(float(2.0))
    print("C")

elif 60 <= sc <= 62:
    print(float(1.7))
    print("C-")

else:
    print(0)
    print("F")
