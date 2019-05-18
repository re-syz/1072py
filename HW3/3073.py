req = int(input())

def return2num(n=0):
    n1 = 1
    n2 = 0
    cur1 = 0
    cur2 = 0

    for i in range(n):
        cur1 += 1
        n1 *= cur1

    for i in range(n):
        cur2 += 1
        n2 += cur2

    return (n1, n2)






ans = return2num(req)
print(ans[0])
print(ans[1])
