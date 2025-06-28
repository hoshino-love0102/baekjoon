t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    count = 0
    for num in range(n, m+1):
        count += str(num).count('0')
    print(count)
