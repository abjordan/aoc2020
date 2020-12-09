#!python

import sys

program_text = open(sys.argv[1], 'r').readlines()

pc = 0
accumulator = 0 

compiled = []
for line in program_text:
    toks = line.strip().split(" ")
    if not len(toks) == 2:
        print(f"HEY - that's not a valid instruction! >>{line.strip()}<<")
    op, arg = toks
    compiled.append([op, int(arg)])

executed = set([])

while True:
    if pc in executed:
        print('About to re-run an instruction. Terminating.')
        print(f'PC = {pc}, ACC = {accumulator}')
        break

    executed.add(pc)

    op, arg = compiled[pc]
    print(f'Executing PC:{pc} ACC:{accumulator} : {op} {arg}')
    if op == 'nop':
        pc += 1
    elif op == 'acc':
        accumulator += arg
        pc += 1
    elif op == 'jmp':
        pc += arg
    else:
        print(f'ERROR: unknown instruction {op} {arg}')
    print(f'Next instruction: {pc} @ {compiled[pc]}')