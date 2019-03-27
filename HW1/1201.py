"""
131072
170318
107-2 Python HW1
1201



"""


# =============

inp = input().split(" ")

# print(inp)

h = int(inp[0])  # head
f = int(inp[1])  # foot

# print(head, foot)


x = 0  # chicken
y = 0  # rabbit


# head = chicken + rabbit
# foot = 2 * chicken + 4 * rabbit

# chicken = head - rabbit
# chicken = (foot - 4 * rabbit) / 2

# x + y = h
# 2x + 4y = f



x1 = (h * 4 - 1 * f)
x2 = (1 * 4 - 1 * 2)


if f % 2 == 0 and h != f:
    if h != f:
        x = int(x1 / x2)
        y = int(h - x)

        print("YES")
        print(x, y)

else:
    print("NO")
