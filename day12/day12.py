#!python

import sys

heading = 90
current_x = 0
current_y = 0

for line in open(sys.argv[1], 'r').readlines():
    instr = line.strip()

    action = instr[0]
    mag = int(instr[1:])

    if action == 'F':
        if heading == 0:
            action = 'N'
        elif heading == 90:
            action = 'E'
        elif heading == 180:
            action = 'S'
        elif heading == 270:
            action = 'W'
        else:
            print(f'Got a FORWARD instruction, but heading is {heading}')
            
    if action == 'N':
        current_y += mag
    elif action == 'S':
        current_y -= mag
    elif action == 'E':
        current_x += mag
    elif action == 'W':
        current_x -= mag
    elif action == 'L':
        heading = (heading - mag) % 360
    elif action == 'R':
        heading = (heading + mag) % 360
    elif action == 'F':
        pass
    else:
        print(f'Unexpected instruction: {instr}')

print(f'Final position: {current_x}, {current_y} with heading {heading}')
print(f'Manhattan distance from origin is { abs(current_x) + abs(current_y) }')