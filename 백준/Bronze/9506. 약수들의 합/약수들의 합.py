while True:
    n = int(input())
    if n == -1:
        break

    p = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            p.append(i)

    if sum(p) == n:
        print(f"{n} =", end=" ")
        for i in range(len(p)):
            print(p[i], end="")
            if i != len(p) - 1:
                print(" + ", end="")
        print()
    else:
        print(f"{n} is NOT perfect.")