n = int(input())
wei = list(map(int, input().split()))
wei.sort()

t = 1
for w in wei:
    if w > t:
        break
    t += w

print(t)