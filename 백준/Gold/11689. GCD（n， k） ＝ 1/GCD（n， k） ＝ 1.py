n = int(input())
r = n
i = 2
while i*i <= n:
    if n%i == 0:
        while n%i == 0:
            n //= i
        r -= r//i
    i += 1
if n > 1:
    r -= r//n
print(r)