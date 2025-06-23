students = set(range(1, 31))

sub = set()
for _ in range(28):
    sub.add(int(input()))

miss = sorted(students - sub)
print(miss[0])
print(miss[1])
