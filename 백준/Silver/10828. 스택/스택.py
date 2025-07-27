N = int(input())
w = [input() for _ in range(N)]
stack = []

for n in w:
    if n[:4] == "push":
        v = int(n[5:])
        stack.append(v)

    elif n == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif n == "size":
        print(len(stack))

    elif n == "empty":
        print(0 if stack else 1)

    elif n == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)