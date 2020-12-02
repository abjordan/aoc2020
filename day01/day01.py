import sys

from functools import reduce
from itertools import combinations

values = []
with open(sys.argv[1], 'r') as fin:
    for line in fin:
        values.append(int(line))

the_pair = None
for c in combinations(values, int(sys.argv[2])):
    if (sum(c)) == 2020:
        the_pair = c
        break

print(f'The pair: {the_pair} --> {reduce(lambda x,y: x*y, the_pair)}')