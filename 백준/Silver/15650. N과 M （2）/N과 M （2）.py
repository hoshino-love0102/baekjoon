n, m = map(int, input().split())

def dfs(s, p):
    if len(p) == m:
        for num in p:
            print(num, end=' ')
        print()
        return

    for i in range(s, n+1):
        dfs(i+1, p+[i])

dfs(1, [])