"""
131072
170318
107-2 Python HW1
1019



"""


# =============

height = int(input())
weight = int(input())

BMI = weight / ((height/100) ** 2)

ana = ["Underweight", "Normal", "Overweight", "Obese Class I", "Obese Class II", "Obese Class III"]

print("%.2f" % BMI)

if BMI < 18.5:
    print(ana[0])
elif 18.5 <= BMI < 24:
    print(ana[1])
elif 24 <= BMI < 27:
    print(ana[2])
elif 27 <= BMI < 30:
    print(ana[3])
elif 30 <= BMI < 35:
    print(ana[4])
elif BMI >= 35:
    print(ana[5])
