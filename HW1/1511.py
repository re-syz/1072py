"""
131072
170318
107-2 Python HW1
1511



"""


# =============

inp = str(input()).split(" ")

n = int(inp[0])
x = int(inp[1])
y = int(inp[2])


ini = 20


# =============  # sol1 - heat -> cooldown

time = 0
for i in range(n):

    if time % 2 == 0:
        ini += x

    else:
        ini -= y

    time += 1

sol1 = ini


# =============  # sol2 - cooldown -> heat

time = 0
ini = 20

for i in range(n - 1):

    if time % 2 == 0:
        ini += x

    else:
        ini -= y

    time += 1

sol2 = ini


# =============  # compare & print

if sol1 >= sol2:
    print(sol1)

else:
    print(sol2)
