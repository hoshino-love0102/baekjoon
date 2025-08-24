n = int(input())
m = int(input())

b = (n // 100) * 100

for i in range(100):
    c = b + i
    if c % m == 0:
        print(f"{i:02d}")
        break
