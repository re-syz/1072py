instr = []

for i in range(5):
    num = 0
    num = int(input())
    instr.append(num)

for i in range(5):
    ans = ""
    ans = str(instr[i]) + "\t" + instr[i] * "*"
    print(ans)
