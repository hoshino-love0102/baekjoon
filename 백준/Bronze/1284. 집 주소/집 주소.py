while True:
    n = input().strip()
    if n == "0":
        break
    w = 2
    
    for d in n:
        if d == "1":
            w += 2
        elif d == "0":
            w += 4
        else:
            w += 3
    
    w += len(n) - 1
    print(w)
