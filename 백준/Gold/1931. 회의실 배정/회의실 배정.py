N = int(input())
m = []

for _ in range(N):
    start, end = map(int, input().split())
    m.append((end, start))

m.sort()

count = 0
end_time = 0

for end, start in m:
    if start >= end_time:
        count += 1
        end_time = end

print(count)
