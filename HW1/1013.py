"""
131072
170318
107-2 Python HW1
1013



"""


# =============

a = float(input())
b = float(input())
math = str(input())
sol = 0.00


if math == "+":
    sol = float(a + b)
    print(str("%.2f" % a) + " + " + str("%.2f" % b) + " = " + str("%.2f" % sol))
elif math == "-":
    sol = float(a - b)
    print(str("%.2f" % a) + " - " + str("%.2f" % b) + " = " + str("%.2f" % sol))
elif math == "*":
    sol = float(a * b)
    print(str("%.2f" % a) + " * " + str("%.2f" % b) + " = " + str("%.2f" % sol))
elif math == "/":
    sol = float(a / b)
    print(str("%.2f" % a) + " / " + str("%.2f" % b) + " = " + str("%.2f" % sol))
