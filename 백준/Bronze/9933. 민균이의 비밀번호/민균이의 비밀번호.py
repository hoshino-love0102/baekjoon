import sys

input = sys.stdin.readline
n = int(input().strip())
a = [input().strip() for _ in range(n)]
s = set(a)

for i in a:
    if i[::-1] in s:
        print(len(i), i[len(i)//2])
        break
