N = int(input())
count = 0
a = set()

for _ in range(N):
    line = input().strip()
    if line == "ENTER":
        a.clear()
    else:
        if line not in a:
            a.add(line)
            count += 1

print(count)