n = int(input())
da = []
final = []
for i in range(n):
    cur = input()

    da.append(cur)
    final.append("Y")


for i in range(len(da)):
    if "(" in da[i]:
        if ")" in da[i]:
            continue

        else:
            final[i] = "N"
    if "[]" in da[i]:
        if "]" in da[i]:
            continue

        else:
            final[i] = "N"
    if "<" in da[i]:
        if ">" in da[i]:
            continue

        else:
            final[i] = "N"
    if "{" in da[i]:
        if "}" in da[i]:
            continue

        else:
            final[i] = "N"


for i in range(len(final)):
    print(final[i])
