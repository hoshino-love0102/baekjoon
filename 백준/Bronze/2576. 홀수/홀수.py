num = [int(input()) for _ in range(7)]

odd = []

for n in num:
    if n % 2 == 1:
        odd.append(n)

if len(odd) > 0:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)
