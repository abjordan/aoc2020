#!python

def run(compiled):
    executed = set([])
    pc = 0
    accumulator = 0 
    return_code = None
    while True:
        if pc in executed:
            print('About to re-run an instruction. Terminating.')
            print(f'PC = {pc}, ACC = {accumulator}')
            return_code = ["INF_LOOP", pc, accumulator]
            break
        executed.add(pc)

        op, arg = compiled[pc]
        #print(f'Executing PC:{pc} ACC:{accumulator} : {op} {arg}')
        if op == 'nop':
            pc += 1
        elif op == 'acc':
            accumulator += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
        else:
            print(f'ERROR: unknown instruction {op} {arg}')
        #print(f'Next instruction: {pc} @ {compiled[pc]}')
        
        if pc == len(compiled):
            print('About to step off the end of the program. Terminating.')
            print(f'PC = {pc}, ACC = {accumulator}')
            return_code = ["NO_LOOP", pc, accumulator]
            break

    return return_code

if __name__ == "__main__":
    import sys
    program_text = open(sys.argv[1], 'r').readlines()

    compiled_prog = []
    for line in program_text:
        toks = line.strip().split(" ")
        if not len(toks) == 2:
            print(f"HEY - that's not a valid instruction! >>{line.strip()}<<")
        op, arg = toks
        compiled_prog.append([op, int(arg)])

    # Try executing it as is - maybe we don't need to change anything?
    ret = run(compiled_prog)
    if ret[0] == "NO_LOOP":
        print(f'It worked! No loop found, PC={ret[1]}, ACC={ret[2]}')
        sys.exit(0)

    # Ok, so that's not likely, because this is AoC
    # There may be a smart way to do this, but there are only
    # about 600 instructions in the test input, sooooo...... 
    # BRUTE FORCE WINS AGAIN!

    for i in range(0, len(compiled_prog)):
        print(f'Checking instruction {i}: {compiled_prog[i]}')
        ret = None
        if compiled_prog[i][0] == 'acc':
            ret = ["INF_LOOP"]
        elif compiled_prog[i][0] == 'jmp':
            new_prog = compiled_prog.copy()
            new_prog[i][0] = 'nop'
            ret = run(new_prog)
            new_prog[i][0] = 'jmp'
        elif compiled_prog[i][0] == 'nop':
            new_prog = compiled_prog.copy()
            new_prog[i][0] = 'jmp'
            ret = run(new_prog)
            new_prog[i][0] = 'nop'
        if ret[0] == "NO_LOOP":
            print(f'Found it! Change instruction {i}.')
            print(f'PC: {ret[1]}, ACC: {ret[2]}')
            break