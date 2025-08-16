s = input().strip()
count = [0] * 26

for ch in s:
    idx = ord(ch) - ord('a')
    count[idx] += 1
    
for i in range(26):
    n = ' ' if i < 25 else '\n'
    print(count[i], end=n)