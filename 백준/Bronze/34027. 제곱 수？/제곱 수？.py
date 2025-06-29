T = int(input())
for _ in range(T):
    n = int(input())
    l = 1
    r = n
    is_square = 0

    while l <= r:
        mid = (l + r) // 2
        square = mid * mid

        if square == n:
            is_square = 1
            break
        elif square < n:
            l = mid + 1
        else:
            r = mid - 1

    print(is_square)