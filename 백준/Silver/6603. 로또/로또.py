def backtrack(start, path):
    if len(path) == 6:
        print(' '.join(map(str, path)))
        return

    for i in range(start, len(s)):
        path.append(s[i])
        backtrack(i + 1, path)
        path.pop()

while True:
    line = input()
    if line == '0':
        break

    parts = list(map(int, line.split()))
    k = parts[0]
    s = parts[1:]

    backtrack(0, [])
    print()