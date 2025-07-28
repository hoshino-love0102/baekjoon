n = int(input())
count = {}

for _ in range(n):
    name = input().strip()
    first = name[0]

    if first in count:
        count[first] += 1
    else:
        count[first] = 1

r = []
for key in count:
    if count[key] >= 5:
        r.append(key)

if r:
    r.sort()
    for ch in r:
        print(ch, end='')
else:
    print("PREDAJA")
