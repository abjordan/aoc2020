#!python

from functools import reduce
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

print(f'Buses       : {buses}')
requirements_raw = [i if raw_buses[i] is not 'x' else None for i in range(0, len(raw_buses))]
requirements = list(filter(lambda b: b != None, requirements_raw))
print('Requirements:', requirements)

# I will confess: I wrote a brute force algorithm that really, really, really didn't work.
# After some Googling, I think this is the Chinese Remainder Theorem.
# I'm working off this: https://brilliant.org/wiki/chinese-remainder-theorem/
# Edit: and this: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python

# The system of congruences is:
#   t === 0 (mod bus_0)
#   t === 1 (mod bus_1)
#   ...
#   t === bus_i - 1 (mod bus_i)
#   ...
#   t === bus_n - n (mod bus_n)
# where === is the congruence operator (i.e., t % bus_n )

def multiplicative_inverse(a, b):
    b0 = b
    x0 = 0
    x1 = 1
    if b == 1: return 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

N = reduce(lambda x, y: x*y, buses)
y = [ N // bus for bus in buses ]

sum = 0
# The trick is that modulus is NOT i -- it's bus# - i
modulus = []
for i in range(0, len(buses)):
    modulus.append(buses[i] - requirements[i])
print(modulus)
for n_i, a_i in zip(buses, modulus):
    p = N // n_i
    sum += a_i *  multiplicative_inverse(p, n_i) * p

result = sum % N
print(f'[2] Part 2: {result}')

# Hmmm... this is wrong because the sign is wrong, I think?