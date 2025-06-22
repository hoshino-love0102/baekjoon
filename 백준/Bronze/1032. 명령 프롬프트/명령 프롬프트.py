n = int(input())
a = [input().strip() for _ in range(n)]

p = list(a[0])

for i in range(1, n):
    for j in range(len(p)):
        if p[j] != a[i][j]:
            p[j] = '?'

print(''.join(p))