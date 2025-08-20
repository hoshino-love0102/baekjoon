N = int(input())

s = 1
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end="")
        
    for j in range(s):
        print("*", end="")
    print()
    s += 2