#!python

from collections import defaultdict
import sys

def speaking_game_map(starters, turn_limit):
    
    spoken = {}

    seq = []
    turn = 1
    last = None
    for num in starters:
        seq.append(num)
        spoken[num] = [turn]
        last = seq[-1]
        turn += 1

    while turn <= (turn_limit):
        last = seq[-1]

        times_spoken = spoken[last]
        if len(times_spoken) == 1:
            next_thing = 0
        else:
            next_thing = spoken[last][-1] - spoken[last][-2]

        if not next_thing in spoken.keys():
            spoken[next_thing] = []
        spoken[next_thing].append(turn)
        seq.append(next_thing)
        turn += 1

        if (turn % 100000 == 0):
            print('.', end='')
            sys.stdout.flush()
    print('')
    return seq[-1]
    

def speaking_game(starters, turn_limit):

    spoken = [None]
    for num in starters:
        spoken.append(num)

    turn = len(starters)
    while turn < turn_limit:
        turn += 1

        if turn % 10000 == 0:
            print(f'------------- Turn {turn}: -------------')
            sys.stdout.flush()
        last_spoken = spoken[-1]
        if last_spoken not in spoken[:-1]:
            #print(f'{last_spoken} ==> Not previously spoken')
            spoken.append(0)
        else:
            last_time = None
            for i, e in reversed(list(enumerate(spoken[:-1]))):
                if e == last_spoken:
                    last_time = i
                    break
            #print(f'{last_spoken} was spoken on {last_time}')
            spoken.append( turn - last_time - 1 )
        #print(f'SPEAK: {spoken[-1]}')

    #print(f'{spoken[-1]}')
    return spoken[-1]


if __name__ == "__main__":
    #starters = [int(x) for x in open(sys.argv[1], 'r').read().strip().split(',')]
    #starters = [int(x) for x in sys.argv[1].strip().split(',')]
    #turn_limit = int(sys.argv[2])

    for starters, turn_limit, expected in [
        [[0,3,6], 10, 0],
        [[0,3,6], 2020, 436],
        [[1,3,2], 2020, 1],
        [[2,1,3], 2020, 10],
        [[1,2,3], 2020, 27],
        [[2,3,1], 2020, 78],
        [[3,2,1], 2020, 438],
        [[3,1,2], 2020, 1836],
        [[16,11,15,0,1,7], 2020, None],
        [[16,11,15,0,1,7], 30000000, None],
    ]:
    #for starters, turn_limit, expected in [
    #    [[0,3,6], 10, 0],
    #]:
        print(f'Sequence: {starters} @ turn {turn_limit}: {speaking_game_map(starters, turn_limit)} (expect {expected})')