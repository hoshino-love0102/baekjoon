n = int(input())
for i in range(n):
    q = input().strip()
    score = 0
    cnt = 0
    for j in q:
        if j == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
