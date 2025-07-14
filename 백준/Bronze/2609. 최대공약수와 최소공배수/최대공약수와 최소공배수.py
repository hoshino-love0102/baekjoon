a, b = map(int, input().split())

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

g = gcd(a, b)
l = a*b//g

print(g)
print(l)
