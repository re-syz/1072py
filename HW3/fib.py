def fib(n):
    n1 = 0
    n2 = 1

    for i in range(n-1):
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth

    return nth
