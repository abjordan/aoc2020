#!python

import sys

lines = open(sys.argv[1], 'r').read()
groups = lines.split("\n\n")

# 26 yes or no questions = 26 bit bitfield

all_yeses = []
n = 0
for group in groups:
    yeses = set([])
    for person in group:
        for c in person.strip():
            yeses.add(c)
    yes_count = len(yeses)
    all_yeses.append(yes_count)
    #print(f'Group {n} = {yes_count}')
    n += 1

answer = sum(all_yeses)
print(f'Sum of counts: {answer}')

everyone_yes = []
n = 0
for group in groups:
    #print('-------')
    people = []
    for person in group.split('\n'):
        p = set(person)
        people.append(p)
        #print('    ',sorted(p))
    isect = set.intersection(*people)
    #print('--->',sorted(isect))
    everyone_yes.append(len(isect))
    #print('Group {} --> {} people'.format(n, len(group.split('\n'))))
    #print(f'Group {n} --> {len(isect)} all-yes')
    n += 1

print(f'Sum of intersections: {sum(everyone_yes)}')