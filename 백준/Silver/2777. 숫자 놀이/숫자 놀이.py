def s(n):
    if n == 1:
        return 1

    dig = []
    for d in range(9, 1, -1):
        while n % d == 0:
            n //= d
            dig.append(d)

    if n != 1:
        return -1

    return len(dig)

T = int(input())
for _ in range(T):
    n = int(input())
    print(s(n))