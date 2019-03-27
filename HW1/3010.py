"""
131072
170318
107-2 Python HW1
3010



"""


# =============

num = int(input())

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num, "is not prime")
           break
   else:
       print(num, "is prime")

else:
   print(num,"is not prime")
