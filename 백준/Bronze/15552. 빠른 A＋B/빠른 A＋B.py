import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    A, B = map(int, input().split())
    print(A + B)
