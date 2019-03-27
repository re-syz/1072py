"""
131072
170318
107-2 Python HW1
1012



"""


# =============

identity = int(input())

if identity == 1 or identity == 2:
    True

else:
    print("roll error")
    exit()

score = int(input())

if 0 <= score <= 100:
    True

else:
    print("score error")
    exit()


# =============

if identity == 1:
    if score >= 60:
        print("pass")
    else:
        print("fail")

else:
    if score >= 70:
        print("pass")
    else:
        print("fail")
