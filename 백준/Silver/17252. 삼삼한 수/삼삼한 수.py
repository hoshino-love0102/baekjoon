N = int(input())

if N == 0:
    print("NO")
else:
    q = False
    p = True
    
    while N > 0:
        digit = N % 3
        if digit == 2:
            p = False
            break
        if digit == 1:
            q = True
        N //= 3
    
    if p and q:
        print("YES")
    else:
        print("NO")