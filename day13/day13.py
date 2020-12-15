#!python

import sys

lines = open(sys.argv[1], 'r').readlines()

net = int(lines[0].strip())
raw_buses = lines[1].strip().split(',')

# Find the bus that has the smallest residual 

not_x = list(filter(lambda b: b != 'x', raw_buses))
buses = [int(b) for b in not_x]
print('Real buses  : ', buses)

residual = [(((net // a_bus)+1) * a_bus) - net for a_bus in buses]

min_residual = min(residual)
min_idx = residual.index(min_residual)
min_bus = buses[min_idx]

retval = min_bus * min_residual
print(f'You should take bus {min_bus} -- waits {min_residual} minutes')
print(f'[1] Part One: bus * wait = {retval}')

# Part Two-----------------------------------------

# Solve for t such that...
#   residual(t, bus_i) = i

#requirement = list(range(0, len(raw_buses))

requirements_raw = [i if raw_buses[i] is not 'x' else None for i in range(0, len(raw_buses))]
requirements = list(filter(lambda b: b != None, requirements_raw))
print('Requirements: ', requirements)

net = 100000000000000
#net = 10000000000
while True:
    deltas = []
    for i in range(0, len(buses)):
        residual_i = ((((net // buses[i])+1) * buses[i]) - net) % buses[i]
        deltas.append(abs(residual_i - requirements[i]))
    
    #print(net, ' --> ', deltas)
    if sum(deltas) == 0:
        print(f'Found a valid time: {net}')
        print(deltas)
        break

    net += 1
    if (net % 10000) == 0:
        print(net)
        sys.stdout.flush()