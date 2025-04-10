t = int(input())

for _ in range(t):
    ps = input()
    c = 0
    a = True

    for char in ps:
        if char == '(':
            c += 1
        else:
            c -= 1

        if c < 0:
            a = False
            break

    if c != 0:
        a = False

    if a:
        print("YES")
    else:
        print("NO")