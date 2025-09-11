number = input().strip()
count = [0]*10

for i in number:
    n = int(i)
    count[n] = count[n] + 1

sn = count[6] + count[9]
if sn % 2 == 0:
    a = sn//2
else:
    a = sn//2 + 1

mx = 0
for d in range(10):
    if d == 6 or d == 9:
        continue
    if count[d] > mx:
        mx = count[d]

if a > mx:
    answer = a
else:
    answer = mx
print(answer)
