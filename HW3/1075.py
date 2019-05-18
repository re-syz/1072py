n9 = input()
n8 = input()

n1 = "../app/" + n9
n2 = "../app/" + n8
fil_1 = open(n1,'r')
fil_2 = open(n2,'r')

fil_1 = fil_1.read().split(" ")
fil_1.pop()
fil_2 = fil_2.read().split(" ")
fil_2.pop()

fil_a = fil_1 + fil_2

for i in range(len(fil_a)):
    fil_a[i] = int(fil_a[i])
fil_a.sort()

for i in range(len(fil_a)):
    if i == len(fil_a) - 1:
        print(fil_a[i], end = " \n")

    else:
        print(fil_a[i], end = " ")
