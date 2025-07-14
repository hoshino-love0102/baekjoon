def gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    a = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            g = gcd(nums[i], nums[j])
            if g > a:
                a = g
    print(a)
