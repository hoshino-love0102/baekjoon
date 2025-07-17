n= list(map(int, input().split()))

a = True
b = True

for i in range(7):
    if n[i] < n[i + 1]:
        b = False
    elif n[i] > n[i + 1]:
        a = False

if a:
    print("ascending")
elif b:
    print("descending")
else:
    print("mixed")