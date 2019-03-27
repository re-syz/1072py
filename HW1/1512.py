"""
131072
170318
107-2 Python HW1
1512



"""


# =============

nk = input().split(" ")
fish = input().split(" ")

for i in range(fish.count("")):
    fish.remove("")

for i in range(len(fish)):
    fish[i] = int(fish[i])


n = int(nk[0])
k = int(nk[1])

# print(n)
# print(k)
# print(fish)


# =============

cur = 0

for i in range(len(fish)):
    need = 0
    need = fish[i] // k

    if need == 0:
        continue

    else:
        cur += k * need

print(cur)
