def largest_diamond(R, C, mine):
    ld = [[0] * C for _ in range(R)]
    rd = [[0] * C for _ in range(R)]
    lu = [[0] * C for _ in range(R)]
    ru = [[0] * C for _ in range(R)]
    
    for i in range(R - 1, -1, -1):
        for j in range(C):
            if mine[i][j] == '1':
                rd[i][j] = 1
                if i < R-1 and j < C-1:
                    rd[i][j] += rd[i + 1][j+1]
                ld[i][j] = 1
                if i < R-1 and j > 0:
                    ld[i][j] += ld[i+1][j-1]
    
    for i in range(R):
        for j in range(C):
            if mine[i][j] == '1':
                lu[i][j] = 1
                if i > 0 and j > 0:
                    lu[i][j] += lu[i-1][j-1]
                ru[i][j] = 1
                if i > 0 and j < C-1:
                    ru[i][j] += ru[i-1][j+1]
    
    max_size = 0
    for i in range(R):
        for j in range(C):
            if mine[i][j] == '0':
                continue
            
            max_possible = min(ld[i][j], rd[i][j])
            
            for k in range(max_possible, 0, -1):
                bottom_i = i + 2*(k-1)
                if bottom_i >= R:
                    continue
                if lu[bottom_i][j] >= k and ru[bottom_i][j] >= k:
                    max_size = max(max_size, k)
                    break
    
    return max_size

R, C = map(int, input().split())
mine = [input().strip() for _ in range(R)]
print(largest_diamond(R, C, mine))