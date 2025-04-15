t = int(input())
a = [0] * 41
b = [0] * 41

a[0], b[0] = 1, 0
a[1], b[1] = 0, 1

for i in range(2, 41):
    a[i] = a[i-1] + a[i-2]
    b[i] = b[i-1] + b[i-2]

for _ in range(t):
    n = int(input())
    print(a[n], b[n])