import sys
input = sys.stdin.readline

N, M = map(int, input().split())

wc = {}

for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

wl = []
for word in wc:
    freq = wc[word]
    wl.append((word, freq))

def s(item):
    word = item[0]
    freq = item[1]
    return (-freq, -len(word), word)

wl.sort(key=s)

for word, _ in wl:
    print(word)
