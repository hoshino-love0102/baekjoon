T = int(input())

for _ in range(T):
    r, s = input().split()
    r = int(r)
    result = ''
    for c in s:
        result += c * r
    print(result)
