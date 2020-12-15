#!python

import sys

# You know what? This problem's much easier
# if we do everything in little-endian bitvectors!

program = open(sys.argv[1], 'r').readlines()

# X1001X becomes:      [] X [1001X]
#                      [] X [1001] X []
#   010010
#   010011
#   110010
#   110011

def bv_to_value(bv):
    sum = 0
    for pow, b in enumerate(bv):
        sum += int(b) * (2**pow)
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

def apply_mask_to_bv(mask, bv):
    new_bv = []
    for i in range(0, len(mask)):
        if mask[i] == '0':
            new_bv.append(bv[i])
        else:
            new_bv.append(mask[i])
    return new_bv

def bv_to_str(bv):
    return ''.join([f'{x}' for x in bv])

def combos(bitstr):
    # Find the first X
    x_pos = bitstr.find('X')
    if x_pos == -1:
        # Didn't find an X, so the only thing we can return is ourself
        return [bitstr]

    # if we found an X, replace it with a 0 then try again
    bitstr_0 = bitstr.replace('X', '0', 1)
    bitstr_1 = bitstr.replace('X', '1', 1)
    return combos(bitstr_0) + combos(bitstr_1) 
            
def masked_addrs(mask, address):
    #print(f'PRE: {bv_to_str(value_to_bv(address))}')
    abv = apply_mask_to_bv(mask, value_to_bv(address))
    #print(f'MSK: {mask}')
    #print(f'ABV: {bv_to_str(abv)}')
    abv_str = ''.join([str(x) for x in abv])
    addr_strs = combos(abv_str)

    addrs = [bv_to_value(addr) for addr in addr_strs]
    return addrs


memory = {}
current_mask = None


#bv = value_to_bv(int(sys.argv[2]))
#print(f'{sys.argv[2]} --> {bv_to_str(bv)}')
#v = bv_to_value(bv)
#print(f'{bv_to_str(bv)} --> {v}')

#mask = "000000000000000000000000000000X1001X"[::-1]
#masked_addrs(mask, 42)
#print('---------------------------------------')
#mask = "00000000000000000000000000000000X0XX"[::-1]
#masked_addrs(mask, 26)

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
    #val_bv = value_to_bv(int(val))

    addrs = masked_addrs(current_mask, int(addr))
    for addr in addrs:
        memory[addr] = int(val)

sum_of_all_values = sum(memory.values()) 
print(f'Sum of all remaining values: {sum_of_all_values}')