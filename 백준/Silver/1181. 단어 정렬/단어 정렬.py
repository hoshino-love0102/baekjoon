n = int(input())
m = set()
for i in range(n):
    m.add(input().strip())
def sort_key(w):
    return (len(w), w)
a = sorted(m, key=sort_key)
for w in a:
    print(w)
