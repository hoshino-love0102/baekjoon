n, m = map(int, input().split())

e = []
p = 1

for _ in range(m):
    e.append((0, p))
    p += 1

for i in range(p, n):
    e.append((i - 1, i))

for a, b in e:
    print(a, b)