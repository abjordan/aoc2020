#!python

import sys

from collections import deque
from itertools import permutations

def check_list(buffer, value):
    # Check to see if there's a pair of values in the list 
    # that sum to value
    for perm in permutations(buffer, 2):
        if value == (perm[0] + perm[1]):
            return True
    return False

def find_contiguous_range(lines, value):
    for i in range(0, len(lines)):
        for j in range(i+1, len(lines)):
            # FWIW, putting this break here cuts execution time by about 10x. Neat!
            if sum(lines[i:j]) > value:
               break
            if sum(lines[i:j]) == value:
                print(f'Found sequence with right sum! From pos:{i} to pos:{j}')
                smallest = min(lines[i:j])
                largest = max(lines[i:j])
                print(f'{smallest} + {largest} = {smallest+largest}')
                return

lines = open(sys.argv[1], 'r').readlines()
LKBK_LEN = int(sys.argv[2])
values = [int(l.strip()) for l in lines]

lookback = deque([], LKBK_LEN)

for value in values:

    if len(lookback) == LKBK_LEN:
        ret = check_list(lookback, value)
        if ret is False:
            print(f'Found first non-sum value: {value}')
            find_contiguous_range(values, value)
            break

    lookback.append(value)