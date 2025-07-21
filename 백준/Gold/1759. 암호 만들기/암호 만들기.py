import sys
L, C = map(int, sys.stdin.readline().split())

chars = sorted(sys.stdin.readline().split())

vowels = {'a', 'e', 'i', 'o', 'u'}

def backtrack(start, password):
    if len(password) == L:
        a = 0
        b = 0
        
        for char in password:
            if char in vowels:
                a += 1
            else:
                b += 1
        
        if a >= 1 and b >= 2:
            print(password)
        
        return

    for i in range(start, C):
        backtrack(i + 1, password + chars[i])

backtrack(0, "")