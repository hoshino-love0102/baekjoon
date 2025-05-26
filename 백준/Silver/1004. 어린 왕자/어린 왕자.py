T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        st = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2
        a = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2
        if st != a:
            count += 1
    print(count)