n = input().strip()
m = input().strip()

cnt = [0] * 26
cnt2 = [0] * 26

for ch in n:
    cnt[ord(ch) - 97] += 1
for ch in m:
    cnt2[ord(ch) - 97] += 1

s = 0
for a, b in zip(cnt, cnt2):
    s += abs(a - b)

print(s)
