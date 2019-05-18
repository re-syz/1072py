from math import factorial

def P(n, m):
    if m > n :
        return 0
    else:
        return int((factorial(n) / factorial(n - m)))

def C(n, m):
    if m > n :
        return 0

    else:
        return int((P(n, m) / factorial(m)))
