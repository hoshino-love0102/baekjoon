def star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    stars = star(n // 2)
    result = []
    space = ' ' * (n // 2)
    
    for line in stars:
        result.append(space + line + space)
        
    for line in stars:
        result.append(line + ' ' + line)

    return result

N = int(input())
output = star(N)
for line in output:
    print(line)