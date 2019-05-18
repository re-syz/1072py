mat = []

for i in range(6):
    cur = input().split(" ")
    if cur[-1] == "":
        cur.pop(3)

    for ii in range(len(cur)):
        cur[ii] = int(cur[ii])
    mat.append(cur)


a = [mat[0],mat[1],mat[2]]
b = [mat[3],mat[4],mat[5]]

# print(a, b)
def matrixMultiPly(a, b) :

    c1 = [a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0],\
          a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1],\
          a[0][0]*b[0][2] + a[0][1]*b[1][2] + a[0][2]*b[2][2]]

    c2 = [a[1][0]*b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0],\
          a[1][0]*b[0][1] + a[1][1]*b[1][1] + a[1][2]*b[2][1],\
          a[1][0]*b[0][2] + a[1][1]*b[1][2] + a[1][2]*b[2][2]]

    c3 = [a[2][0]*b[0][0] + a[2][1]*b[1][0] + a[2][2]*b[2][0],\
          a[2][0]*b[0][1] + a[2][1]*b[1][1] + a[2][2]*b[2][1],\
          a[2][0]*b[0][2] + a[2][1]*b[1][2] + a[2][2]*b[2][2]]


    c = [c1, c2, c3]
    return c

for li in matrixMultiPly(a, b):
    print(li)
