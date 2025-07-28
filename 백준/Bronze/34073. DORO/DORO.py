n = int(input())
words = input().split()

for i in range(n):
    word = words[i]
    d = word + 'DORO'
    if i < n - 1:
        print(d, end=' ')
    else:
        print(d, end='\n')