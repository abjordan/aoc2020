#!python

import sys

# So I think there's a nice closed-form solution to this 
# problem. It's a binary tree traversal, or maybe even a
# simple binary encoding?

# There are 128 rows on the plane, and then 8 seats in each row.
# The row is easy: RLR means right, left, right - 101, which is 
# seat 5. In fact, the seat ID is rows * 8 + seat, which is 
# (row << 3) + seat, which is the full string. LOL - nice puzzle.
#
# F = 0, B = 1
# L = 0, R = 1
#
# Example input: BFFFBBFRRR --> 567
#                1000110111 ==  567

intable = "FBLR"
outtable = "0101"
table = str.maketrans(intable, outtable)

seats = set([])
for line in open(sys.argv[1], 'r').readlines():
    b_str = line.strip().translate(table)
    seat_val = int(b_str, 2)
    #print(f'{line.strip()} --> {b_str} --> {seat_val}')
    seats.add(seat_val)

min_seat = min(seats)
max_seat = max(seats)
print(f'Min seat value: {min_seat}')
print(f'Max seat value: {max_seat}')

# Find the missing seat
all_seats = set(range(min_seat, max_seat))
missing_seat = all_seats - seats
print(f'Missing seat: {missing_seat}')