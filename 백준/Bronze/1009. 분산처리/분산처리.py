def m(a, b, mod):
    result = 1
    a = a% mod
    while b > 0:
        if b % 2 == 1:
            result=(result*a)%mod
        a=(a*a)%mod
        b//=2
    return result

a = int(input())
for _ in range(a):
    a, b = map(int, input().split())
    n = m(a, b, 10)
    if n == 0:
        n = 10
    print(n)
