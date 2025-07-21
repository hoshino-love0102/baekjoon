import sys

try:
    N = int(sys.stdin.readline())
except (IOError, ValueError):
    N = int(input())

d = []

def dfs(c):
    d.append(c)
    
    a = c % 10
    for i in range(a):
        new_num = c * 10 + i
        dfs(new_num)

for i in range(10):
    dfs(i)

d.sort()

if N >= len(d):
    print(-1)
else:
    print(d[N])