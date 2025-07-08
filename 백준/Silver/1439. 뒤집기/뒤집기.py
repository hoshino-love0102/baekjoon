s = input().strip()

c = 0

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        c += 1

n = c + 1

if s[0] == '0':
    count0 = (n + 1) // 2
    count1 = n // 2
else:
    count1 = (n + 1) // 2
    count0 = n // 2

print(min(count0, count1))