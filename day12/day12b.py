#!python

import sys

heading = 90
current_x = 0
current_y = 0

wp_delta_x = 10
wp_delta_y = 1

for line in open(sys.argv[1], 'r').readlines():
    
    #print(f'({current_x},{current_y}) -- WP ({wp_delta_x}, {wp_delta_y})', end='')
    instr = line.strip()

    action = instr[0]
    mag = int(instr[1:])

    if action == 'N':
        wp_delta_y += mag
    elif action == 'S':
        wp_delta_y -= mag
    elif action == 'E':
        wp_delta_x += mag
    elif action == 'W':
        wp_delta_x -= mag
    elif action == 'L':
        mag = mag % 360
        # Rotate mag degrees CCW
        if mag == 90:
            wp_delta_x, wp_delta_y = [-1 * wp_delta_y, wp_delta_x]
        elif mag == 180:
            wp_delta_x, wp_delta_y = [-1 * wp_delta_x, -1 * wp_delta_y]
        elif mag == 270:
            wp_delta_x, wp_delta_y = [wp_delta_y, -1 * wp_delta_x]
        else:
            print(f'Non right angle rotation: {mag}')
    elif action == 'R':
        mag = mag % 360
        # Rotate mag degrees CCW
        if mag == 270:
            wp_delta_x, wp_delta_y = [-1 * wp_delta_y, wp_delta_x]
        elif mag == 180:
            wp_delta_x, wp_delta_y = [-1 * wp_delta_x, -1 * wp_delta_y]
        elif mag == 90:
            wp_delta_x, wp_delta_y = [wp_delta_y, -1 * wp_delta_x]
        else:
            print(f'Non right angle rotation: {mag}')
    elif action == 'F':
        current_x += mag * wp_delta_x
        current_y += mag * wp_delta_y
    else:
        print(f'Unexpected instruction: {instr}')

    #print(f'===> {instr} ===> ({current_x},{current_y}) -- WP ({wp_delta_x}, {wp_delta_y})')

print(f'Final WP delta: {wp_delta_x}, {wp_delta_y}')
print(f'Final position: {current_x}, {current_y} with heading {heading}')
print(f'Manhattan distance from origin is { abs(current_x) + abs(current_y) }')