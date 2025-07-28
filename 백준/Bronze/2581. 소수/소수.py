m = int(input())
n = int(input())
p = []

def sosuh(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if sosuh(i):
        p.append(i)

if p:
    print(sum(p))
    print(min(p))
else:
    print(-1)