"""
131072
170318
107-2 Python HW1
3032



"""


# =============

con = []
con_copy = []

while True:
    n = input()

    try:
        n = float(n)

    except:
        if n == "q":
            break

        else:
            print("Please Enter Numbers Only")

    else:
        n = float(n)
        if int(n) == float(n):
            con.append(int(n))

        else:
            con.append(float(n))

for i in range(len(con)):
    con_copy.append(con[i])


print(con)
con.sort()
print(con)
con.sort(reverse = True)
print(con)
print(con_copy)
