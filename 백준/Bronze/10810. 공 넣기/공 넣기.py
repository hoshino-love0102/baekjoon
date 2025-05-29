n, m = map(int, input().split())
b = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        b[idx] = k

print(' '.join(map(str, b)))