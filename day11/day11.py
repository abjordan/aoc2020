#!python

import hashlib
import sys

def hash_board(board):
    board_hash = hashlib.md5()
    for row in board:
        row_hash = hashlib.md5(''.join(row).encode('utf-8')).digest()
        board_hash.update(row_hash)
    return board_hash.hexdigest()

def count_neighbors(board, i, j):
    rows = len(board)
    cols = len(board[0])

    nw = board[i-1][j-1] if ((i > 0) and (j > 0)) else ''
    n  = board[i-1][j]   if (i > 0) else ''
    ne = board[i-1][j+1] if ((i > 0) and (j < (cols-1))) else ''
    w  = board[i][j-1]   if (j > 0) else ''
    e  = board[i][j+1]   if (j < (cols-1)) else ''
    sw = board[i+1][j-1] if ((i < (rows-1)) and (j > 0)) else ''
    s  = board[i+1][j]   if (i < (rows-1)) else ''
    se = board[i+1][j+1] if ((i < (rows-1)) and (j < (cols-1))) else ''
    
    neighbors = [nw, n, ne, w, e, sw, s, se]
    n_c = sum([ 1 if x == '#' else 0 for x in neighbors])
    #print(i, j, n_c, neighbors)
    return n_c

def count_los_neighbors(board, i, j):
    rows = len(board)
    cols = len(board[0])
    #print(i,j)
    # Scan north
    r = i-1
    n = '_'
    while r >= 0:
        if board[r][j] == '.': 
            r -= 1
        else:
            n = board[r][j]
            break
    
    # Scan south
    r = i+1
    s = '_'
    while r < rows:
        if board[r][j] == '.':
            r += 1
        else:
            s = board[r][j]
            break

    # Scan west
    c = j-1
    w = '_'
    while c >= 0:
        if board[i][c] == '.':
            c -= 1
        else:
            w = board[i][c]
            break

    # Scan east
    c = j+1
    e = '_'
    while c < cols:
        if board[i][c] == '.':
            c += 1
        else:
            e = board[i][c]
            break

    # Scan NW
    r = i-1
    c = j-1
    nw = '_'
    while (r >= 0) and (c >= 0):
        if board[r][c] == '.':
            r -= 1
            c -= 1
        else:
            nw = board[r][c]
            break

    # NE
    r = i-1
    c = j+1
    ne = '_'
    while (r >= 0) and (c < cols):
        if board[r][c] == '.':
            r -= 1
            c += 1
        else:
            ne = board[r][c]
            break

    # SW
    r = i+1
    c = j-1
    sw = '_'
    while (r < rows) and (c >= 0):
        if board[r][c] == '.':
            r += 1
            c -= 1
        else:
            sw = board[r][c]
            break

    # SE
    r = i+1
    c = j+1
    se = '_'
    while (r < rows) and (c < cols):
        if board[r][c] == '.':
            r += 1
            c += 1
        else:
            se = board[r][c]
            break
   
    #print(nw, n, ne)
    #print(w, '@', e)
    #print(sw, s, se)

    neighbors = [nw, n, ne, w, e, sw, s, se]
    n_c = sum([ 1 if x == '#' else 0 for x in neighbors])
    return n_c
    

def read_board(filename):
    board_lines = open(filename, 'r').readlines()

    board = []
    for line in board_lines:
        line = list(line.strip())
        board.append(line)

    return board

def evolve(board):
    # Rules: 
    #   if seat is empty (L) and no occupied seats adjacent --> occupied (#)
    #   if seat is occupied (#) and four or more seats are occupied --> L
    #   floors (.) never change
    # Note that we can't do the updates during the loop, as that would put
    # the board into an inconsistent state
    updates = {}
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == '.':
                continue

            # For Part A:
            #c = count_neighbors(board, i, j)
                
            # For Part B:
            c = count_los_neighbors(board, i, j)
            if board[i][j] == 'L':
                if c == 0:
                    updates[(i,j)] = '#'
            elif board[i][j] == '#':
                if c > 4:
                    updates[(i,j)] = 'L'
    for c, newval in updates.items():
        #print(c, newval)
        board[c[0]][c[1]] = newval

# Conway's Game of Seats?

if __name__ == "__main__":
    
    board = read_board(sys.argv[1])

    current_hash = None
    last_hash = None
    generations = 0

    print('Starting board:')
    for r in board:
        print(''.join(r))
    print('--------------------')

    while True:
        generations += 1
        evolve(board)
        current_hash = hash_board(board)
        print(f'Generation {generations}')
        #for r in board:
        #    print(''.join(r))
        #print('--------------------')
        #if generations > 10:
        #    break
        if current_hash == last_hash:
            break
        last_hash = current_hash

    occ = 0
    for i in range(0, len(board)):
        occ += sum([1 if x == '#' else 0 for x in board[i]])

    print(f'Finished after {generations} generations')
    print(f'{occ} seats are occupied')