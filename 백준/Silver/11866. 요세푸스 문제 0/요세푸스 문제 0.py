n, k = map(int, input().split())

visit = [False] * (n + 1)
c = 0
a = 0
print("<", end="")

while c < n:
    step = 0
    while step < k:
        a += 1
        if a > n:
            a = 1
        if not visit[a]:
            step += 1

    visit[a] = True
    c += 1

    print(a, end="")
    if c < n:
        print(", ", end="")

print(">")
