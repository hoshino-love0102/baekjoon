words = [input() for _ in range(5)]
mx = max(len(i) for i in words)

for i in range(mx):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')
