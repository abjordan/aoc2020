#!python

import sys

# You know what? This problem's much easier
# if we do everything in little-endian bitvectors!

program = open(sys.argv[1], 'r').readlines()

def bv_to_value(bv):
    sum = 0
    for pow, b in enumerate(bv):
        sum += b * (2**pow)
    return sum

def value_to_bv(value):
    curr = value
    bv = []
    while curr != 0:
        bv.append(curr % 2)
        curr = curr >> 1
    if len(bv) < 36:
        bv += [0]*(36 - len(bv))
    return bv

def apply_mask_to_bv(bv, mask):
    new_bv = list(bv)
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            continue
        else:
            new_bv[i] = int(mask[i])
    return bv_to_value(new_bv)

def bv_to_str(bv):
    return ''.join([f'{x}' for x in bv])

memory = {}
current_mask = None


#bv = value_to_bv(int(sys.argv[2]))
#print(f'{sys.argv[2]} --> {bv_to_str(bv)}')
#v = bv_to_value(bv)
#print(f'{bv_to_str(bv)} --> {v}')

for line in program:
    op, val = [x.strip() 
                for x in line.strip().split('=')]
    if op == 'mask':
        #print('UPDATE MASK')
        le_val = val[::-1]
        #print(le_val)
        current_mask = le_val
        continue

    addr = op.split('[')[1].split(']')[0]
    val_bv = value_to_bv(int(val))
    masked_val = apply_mask_to_bv(val_bv, current_mask)
    #print(f'{val} --> {masked_val}')
    memory[addr] = masked_val

sum_of_all_values = sum(memory.values()) 
print(f'Sum of all remaining values: {sum_of_all_values}')