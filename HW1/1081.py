"""
131072
170318
107-2 Python HW1
1081



"""


# =============

n = int(input())

Tom = 1
Jerry = n
winner = ""

while True:
    if Tom + 1 != Jerry:
        Tom += 1

    else:
        winner = "Tom"
        break

    if Jerry - 1 != Tom:
        Jerry -= 1

    else:
        winner = "Jerry"
        break

print(winner)
