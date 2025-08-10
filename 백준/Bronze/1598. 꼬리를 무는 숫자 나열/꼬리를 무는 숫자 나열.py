a, b = map(int, input().split())

x,y = (a-1)//4, (a-1)%4
p,q = (b-1)//4, (b-1)%4

d = abs(x - p) + abs(y - q)
print(d)
