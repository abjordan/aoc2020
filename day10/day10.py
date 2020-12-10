#!python

import functools
import sys

raw_in = open(sys.argv[1], 'r').readlines()
adapters = [ int(x.strip()) for x in raw_in ]

ordered = sorted(adapters)

# Add in the outlet
ordered.insert(0, 0)

# Add in our device as the last step
ordered.append( ordered[-1] + 3)

#print(ordered)
diffs = [ ordered[x+1] - ordered[x] for x in range(0, len(ordered)-1)]
#print(diffs)

ones = sum([ 1 if x == 1 else 0 for x in diffs])
threes = sum([ 1 if x == 3 else 0 for x in diffs])
#print(ones, threes)
print(f'[1] Ones times threes: {ones * threes}')

# Part 2: how many different ways can the adapters be arrange?
# Connectors only work when the difference is 0, 1, 2, or 3.
# So, if there's a jump of three between two adapters, we can't
# remove either side of that jump. For example, in the 
# test input, we always have to have 12,15 in the sequence.
# It's really a matter of how many ways you can use the sequences
# of 1-jumps. After that, you can just multiply them together.

# (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#    1,  3, 1, 1, 1, 3,  1,  1,  3,  1,  3,  3
#          ---------   ----------  -------
#             4           2          1
#
# 3,1,3         is the only choice
# 3,1,1,3       two: can  3,1a,3 and 3,1b,3
# 3,1,1,1,3     four: can remove one of the interior two
# 3,1,1,1,1,3   

#      3  1  3              1 --> 1
# 0, 1, 4, 5, 8

#      3  1  1  3           2 --> 2
# 0, 1, 4, 5, 6, 9

#      3  1  1  1  3        3 --> 4
# 0, 1, 4, 5, 6, 7, 10

#      3  1  1  1  1  3     4 --> 7
# 0 1 4 5 6 7 8 11
#   1 4 5 6 7 8 11
#   1 4 5 6   8 11
#   1 4 5     8 11
#   1 4   6 7 8 11
#   1 4   6   8 11
#   1 4     7 8 11

def list_split(l, item):
    runs = []
    piece = []
    for i in range(0, len(l)):
        if l[i] == 1:
            piece.append(l[i])
        elif l[i] == 3:
            if len(piece) != 0:
                runs.append(piece)
            piece = []
    return runs

sequences = list_split(diffs, 3)

# Guess what? My input only had runs as long as 4
lookup = {
    1: 1,
    2: 2,
    3: 4,
    4: 7
}

count = 1
for seq in sequences:
    #print(len(seq))
    count *= lookup[len(seq)]
print(f'[2] Combinations: {count}')