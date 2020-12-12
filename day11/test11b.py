#!python

import day11
board = day11.read_board('los_test_2.txt')
c11 = day11.count_los_neighbors(board, 1, 1)
print(f'c(1,1) = {c11}')
c13 = day11.count_los_neighbors(board, 1, 3)
print(f'c(1,3) = {c13}')
c41 = day11.count_los_neighbors(board, 4, 1)
print(f'c(4,1) = {c41}')
c66 = day11.count_los_neighbors(board, 6, 5)
print(f'c(6,6) = {c66}')