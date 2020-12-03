import sys
import re

pattern = re.compile(r'(\d+)-(\d+) ([a-z]+): ([a-z]+)')

valid_a = 0
valid_b = 0
for line in open(sys.argv[1]).readlines():
    
    m = pattern.match(line.strip())
    [low, high, ch, password] = m.groups()
    
    # Wow - this is 100% the wrong way to do this!
    # This code finds all the ones that have the 
    # character _repeated_ a valid number of times, 
    # but the brief is for a raw frequency count. I 
    # like the idea of building a regex on the fly
    # though, so the code stays!
    #
    #new_re = f'{ch}{{{low},{high}}}'
    #checker = re.compile(new_re)
    #if checker.search(password) is not None:
    #    valid += 1
    
    # Part A: ch must appear anywhere in the password
    # between low and high times, inclusive.
    count = sum([1 if x == ch else 0 for x in password])
    if int(low) <= count and count <= int(high):
        valid_a += 1

    # Part B: exactly one of the characters at low or high
    # must equal ch. Are there better ways to do this? Yes.
    # Does this work? Also yes. (Note that it's 1-indexed.)
    idx_low = int(low)
    idx_high = int(high)
    ch1 = (password[idx_low-1] == ch)
    ch2 = (password[idx_high-1] == ch)
    valid_b += 1 if (ch1 ^ ch2) else 0

print(f'Found {valid_a} valid lines for Part A')
print(f'Found {valid_b} valid lines for Part B')