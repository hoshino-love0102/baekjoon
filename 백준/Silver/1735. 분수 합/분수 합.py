def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
C, D = map(int, input().split())

n = A * D + B * C
m = B * D

g = gcd(n, m)

print(n // g, m // g)