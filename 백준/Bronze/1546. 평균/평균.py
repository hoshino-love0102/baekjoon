n = int(input())
score = list(map(int, input().split()))

m = max(score)
n_score = []

for s in score:
    n_score.append(s / m * 100)

avg = sum(n_score) / n
print(avg)
