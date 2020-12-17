#!python

import sys

input = open(sys.argv[1], 'r').read()

classes, mine, nearby = input.split('\n\n')

valid_ranges = []

class_to_range = {}

for clz in classes.split('\n'):
    name, values = clz.strip().split(':')
    first, or_str, second = values.strip().split(' ')
    f_low, f_high = [int(x) for x in first.split('-')]
    s_low, s_high = [int(x) for x in second.split('-')]
    valid_ranges.append( (f_low, f_high) )
    valid_ranges.append( (s_low, s_high) )
    class_to_range[name] = [(f_low, f_high), (s_low, s_high)]

# So we could be efficient about this, or we could try to find overlapping
# ranges. There's only 20 classes in the challenge input, and each line
# has 20 values on it, so that's at most 400 checks per line. We could
# also be clever and skip ranges we've already found a match for... but
# do we need to?

# Part 1: Ignore your own ticket. Find sum of values that are not in
# valid as a value for any field.
error_rate = 0
valid_tickets = []
tickets = nearby.strip().split('\n')[1:]    # Skip the "nearby tickets:" line
for ticket in tickets:
    fields = [int(f) for f in ticket.strip().split(',')]
    all_valid = True
    for field in fields:
        valid = False
        # We can break out of this loop once we find one that matches
        for (low, high) in valid_ranges:
            if field >= low and field <= high:
                valid = True
                break
        if not valid:
            error_rate += field
        all_valid &= valid
    if all_valid:
        valid_tickets.append(ticket)

print(f'Ticket error rate is {error_rate}')

# Part 2: Figure out the mapping of fields. Brute force is singing its sweet
# sweet siren call, once again. There are, unfortunately, 2,432,902,008,176,640,000
# possible permutations of 20 fields, so that's not going to work.

print(f'Found {len(valid_tickets)} valid tickets out of {len(tickets)}')

# Look at the first column for every ticket and find a set of names that 
# all the tickets are valid for.

from collections import defaultdict
valid_assignments = defaultdict(list)

parsed_tickets = []
for ticket in tickets:
    parsed_tickets.append( [int(f) for f in ticket.strip().split(',')] )

# Go through each column and figure out which possible fields it could be
for i in range(0, len(parsed_tickets[0])):
    for clz, rng in class_to_range.items():
        #print(f'Checking if {clz} works for field {i} -- {rng}: ', end='')
        valid = True
        for ticket in parsed_tickets: 
            if (ticket[i] >= rng[0][0] and ticket[i] <= rng[0][1]) or \
                (ticket[i] >= rng[1][0] and ticket[i] <= rng[1][1]):
                pass
            else:
                valid = False
        if valid:
            valid_assignments[clz].append(i)
        else:
            pass
            #print('INVALID!')

# At this point we have a list of possible assignments. For any of them
# that only have a single possibility, we can eliminate that value for
# every other field. E.g., if class = [1, 2] and seat = [2], then we can
# get rid of 2 from class's list

print(valid_assignments)

assigned = set([])

for clz, possibles in valid_assignments.items():
    if len(possibles) == 1:
        assigned.add(clz)

print(assigned)

# Wow -- that *really* doesn't work. Back to the drawing board...