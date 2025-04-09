N = int(input())
num = list(map(int, input().split()))
v = int(input())

c = 0
for num in num:
    if num == v:
        c += 1

print(c)