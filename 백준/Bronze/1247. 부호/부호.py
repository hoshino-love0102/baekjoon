import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    tot = 0
    for _ in range(n):
        num = int(input())
        tot += num
    if tot > 0:
        print("+")
    elif tot < 0:
        print("-")
    else:
        print("0")
