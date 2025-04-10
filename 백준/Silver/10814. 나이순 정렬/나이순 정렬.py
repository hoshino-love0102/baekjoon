n = int(input())
m = []

for _ in range(n):
    age_name = input().split()
    age = int(age_name[0])
    name = age_name[1]
    m.append((age, name))

m.sort(key=lambda x: x[0])

for m2 in m:
    print(m2[0], m2[1])
