N, M = map(int, input().split())
v = [False] * (N + 1)
s = []

def backtrack():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if not v[i]:
            v[i] = True
            s.append(i)
            backtrack()
            s.pop()
            v[i] = False

backtrack()
