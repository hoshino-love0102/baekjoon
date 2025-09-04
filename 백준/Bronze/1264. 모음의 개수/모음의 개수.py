while True:
    line = input().rstrip()
    if line == "#":
        break

    v = "aeiouAEIOU"
    c = 0
    
    for ch in line:
        if ch in v:
            c += 1

    print(c)
