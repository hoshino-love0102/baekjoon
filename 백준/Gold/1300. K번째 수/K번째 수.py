N = int(input())
k = int(input())

l = 1
r = k
a = 0

while l <= r:
    mid = (l + r) // 2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid // i, N)

    if cnt < k:
        l = mid + 1
    else:
        a = mid
        r = mid - 1

print(a)
