a = ['E', 'A', 'B', 'C', 'D']

for i in range(3):
    n = list(map(int, input().split()))
    m = n.count(0)
    print(a[m])
