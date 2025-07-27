n, k = map(int, input().split())
t = []

for i in range(n):
    row = [1] * (i+1)
    for j in range(1, i):
        row[j] = t[i-1][j-1] + t[i-1][j]

    t.append(row)
print(t[n-1][k-1])