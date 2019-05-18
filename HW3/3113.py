def add(*nums):
    ans = 0
    for i in range(len(nums)):
        ans += nums[i]

    return ans


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add(n1, n2, n3))

n4 = int(input())
n5 = int(input())

print(add(n4, n5))
