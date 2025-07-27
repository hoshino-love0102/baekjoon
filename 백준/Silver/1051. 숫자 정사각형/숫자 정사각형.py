n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

m_size = 1

for i in range(n):
    for j in range(m):
        for l in range(1, min(n-i, m-j)):
            if grid[i][j] == grid[i][j+l] == grid[i+l][j] == grid[i+l][j+l]:
                m_size = max(m_size, (l + 1) ** 2)

print(m_size)