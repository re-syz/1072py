"""
131072
170318
107-2 Python HW1
1102



"""


# =============

n = int(input())
m = int(input())

# for i in range(1, n + 1):
#     for ii in range(1, m + 1):
#
#         if ii != m and i != n:
#             print(str(i) + "*" + str(ii) + "=" + "%2d" % (i * ii), end = " ")
#
#         elif ii == m and i != n:
#             print(str(i) + "*" + str(ii) + "=" + "%2d" % (i * ii), end = " \n")
#
#         elif ii != m and i == n:
#             print(str(i) + "*" + str(ii) + "=" + "%2d" % (i * ii), end = " ")
#
#         else:
#             print(str(i) + "*" + str(ii) + "=" + "%2d" % (i * ii))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print("%d*%d=%2d" % (i,j,i*j),end=" ")

    print("")
