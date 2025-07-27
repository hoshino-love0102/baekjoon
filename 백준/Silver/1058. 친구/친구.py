N = int(input())
friend = [list(input().strip()) for _ in range(N)]

m = 0
for i in range(N):
    count = 0
    for j in range(N):
        if i == j:
            continue
        if friend[i][j] == 'Y':
            count += 1
        else:
            for k in range(N):
                if friend[i][k] == 'Y' and friend[k][j] == 'Y':
                    count += 1
                    break
                    
    m = max(m, count)
    
print(m)