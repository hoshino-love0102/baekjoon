a = 0
b = 0

for i in range(9):
    num = int(input())
    if num > a:
        a = num
        b = i + 1

print(a)
print(b)
