eng = "zabcdefghijklmnopqrstuvwxy"

cod = input().split("-")
for i in range(len(cod)):
    cod[i] = int(cod[i])


msg = ""

for i in range(len(cod)):
    cur = cod[i]
    cur_char = ""

    n1 = cur // 26
    n2 = cur % 26

    if n1 >= 1:

        if n2 == 0:  # z
            for i in range(n1):
                cur_char += eng[n2]

        else:  # not z
            for i in range(n1 + 1):
                cur_char += eng[n2]

    else:
        cur_char = eng[n2]

    msg += cur_char

print(msg)
