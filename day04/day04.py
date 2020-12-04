import re
import sys

lines = open(sys.argv[1], 'r').read()

records = lines.split("\n\n")

def check_height(x):
    if not len(x) >= 4:
        return False
    unit = x[-2:]
    hgt = int(x[:-2])
    if unit == "in":
        return (hgt >= 59 and hgt <= 76)
    elif unit == "cm":
        return (hgt >= 150 and hgt <= 193)
    else:
        return False

checkers = {
    "byr": lambda x: int(x) >= 1920 and int(x) <= 2002,
    "iyr": lambda x: int(x) >= 2010 and int(x) <= 2020,
    "eyr": lambda x: int(x) >= 2020 and int(x) <= 2030,
    "hgt": check_height,
    "hcl": lambda x: re.match(r'#[0-9a-f]{6}', x) != None,
    "ecl": lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    "pid": lambda x: re.match(r'^[0-9]{9}$', x) != None,
    "cid": lambda x: True
}

required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
valid = 0
total = 0

for record in records:
    total += 1
    text = " ".join(record.split("\n"))
    tokens = text.split(" ")

    r = {}
    for tok in tokens:
        subtok = tok.split(":")
        if not len(subtok) == 2:
            print("---------------------------")
            print(text)
            print(f"invalid field: {tok}")
        r[subtok[0]] = subtok[1]

    found = set(r.keys())
    if not required.issubset(found):
        print("---------------------------")
        print(text)
        print(f"invalid: missing {required - found}")
    else:
        good = True
        for field, value in r.items():
            chk = checkers[field](value)
            r[field] = [value, chk]
            good &= chk

        if good:
            valid += 1
        else:
            print("---------------------------")
            print(text)
            print("invalid: failed constraints")
            print(r)
            
print(f"Found {valid}/{total} valid records")