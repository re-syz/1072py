n1 = input()

nf = "./" + n1

fil = open(nf , 'r').readlines()

for i in range(len(fil)):
    fil[i] = fil[i].lower()

    if i != len(fil) - 1:
        fil[i] = fil[i].replace("\n", "")


book_name = []
book = []

for order in fil:
    bk = order.split(",")

    cur = ""
    cur = bk[0]

    req = 0
    req = int(bk[1])

    if cur not in book_name:
        book_name.append(cur)
        book.append([cur, req])

    else:
        for i in range(len(book)):
            if book[i][0] == cur:
                book[i][1] += req


book_name.sort()
# print(book_name)

for i in range(len(book_name)):
    cur = ""
    cur = book_name[i] + ","

    tot = 0
    for ii in range(len(book)):
        if book_name[i] == book[ii][0]:
            tot = book[ii][1]

    cur += str(tot)

    print(cur)
