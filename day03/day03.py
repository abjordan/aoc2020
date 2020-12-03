import sys

def ski(board, right, down):
    i, j = 0, 0
    hits = 0
    for i in range(0, rows, down):
        if board[i][j] == "#":
            hits += 1
        j = (j + right) % len(board[i])
    return hits


# Slope is right 3, down 1
board = []
rows = 0
for line in open(sys.argv[1], 'r').readlines():
    board.append(list(line.strip()))
    rows += 1

r1d1 = ski(board, 1, 1)
r3d1 = ski(board, 3, 1)
r5d1 = ski(board, 5, 1)
r7d1 = ski(board, 7, 1)
r1d2 = ski(board, 1, 2)

hits = r1d1 * r3d1 * r5d1 * r7d1 * r1d2

print(f'With the given board at r3/d1, you will hit {r3d1} trees')
print(f'Part B: {hits}')