n,b = map(int, input().split())

r = []

while n > 0:
    a = n % b
    if a < 10:
        r.append(chr(a + ord('0')))
    else:
        r.append(chr(a - 10 + ord('A')))
    n = n//b
for i in range(len(r)-1, -1, -1):
    print(r[i], end="")
print()