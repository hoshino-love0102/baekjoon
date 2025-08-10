n = int(input())
times = list(map(int, input().split()))
x = 0
y = 0

for t in times:
    x += ((t // 30) + 1) * 10
    y += ((t // 60) + 1) * 15

if x < y:
    print(f"Y {x}")
elif y < x:
    print(f"M {y}")
else:
    print(f"Y M {x}")
