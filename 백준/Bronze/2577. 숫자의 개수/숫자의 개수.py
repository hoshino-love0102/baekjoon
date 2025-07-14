a = int(input())
b = int(input())
c = int(input())

result = a * b * c
k = str(result)

count = [0] * 10

for d in k:
    count[int(d)] += 1

for i in range(10):
    print(count[i])