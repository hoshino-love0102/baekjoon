board = []
for _ in range(8):
    row = input()
    board.append(row)

count = 0

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            if board[i][j] == 'F':
                count += 1

print(count)