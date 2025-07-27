import sys

N = int(sys.stdin.readline())
p = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    p.append((x, y))

p.sort()

for x, y in p:
    print(x, y)