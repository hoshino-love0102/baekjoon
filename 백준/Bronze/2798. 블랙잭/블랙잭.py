from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for comb in combinations(cards, 3):
    tot = sum(comb)
    if tot <= m:
        max_sum = max(max_sum, tot)

print(max_sum)