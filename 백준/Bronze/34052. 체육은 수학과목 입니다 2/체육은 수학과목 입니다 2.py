times = [int(input()) for _ in range(4)]
tot = sum(times) + 300

if tot <= 1800:
    print("Yes")
else:
    print("No")