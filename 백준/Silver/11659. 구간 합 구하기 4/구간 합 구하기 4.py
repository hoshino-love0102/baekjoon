import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
m = int(data[1])

num = list(map(int, data[2:2+n]))

p = [0] * (n+1)
for i in range(1, n+1):
    p[i] = p[i-1] + num[i-1]

idx = 2 + n

for _ in range(m):
    a = int(data[idx])
    b = int(data[idx + 1])
    print(p[b] - p[a - 1])
    idx += 2