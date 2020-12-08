import re

def get_clean_data():
    import os

    # get input file path
    file_path = os.path.join(os.getcwd(), 'input.txt')

    # read input file data as list of lines
    with open(file_path) as f:
        lines = f.readlines()

    # clean lines - remove new line character
    lines = [line.replace('\n','') for line in lines]

    return lines

passports = get_clean_data()

# define challenge variables
mandatory_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Part 1

valid_passports_p1 = 0
current_keys = []

for index, line in enumerate(passports):
    if line == '':
        all_mandatory = all(key in current_keys for key in mandatory_keys)
        if all_mandatory:
            valid_passports_p1 += 1
        current_keys = []
    else:
        elements = line.split()
        for element in elements:
            key = element.split(':')[0]
            current_keys.append(key)

    if index == (len(passports) - 1):
        all_mandatory = all(key in current_keys for key in mandatory_keys)
        if all_mandatory:
            valid_passports_p1 += 1

print("Part 1 Answer:", valid_passports_p1)

# Part 2

def is_valid(item):
    key = item[0]
    value = item[1]

    if key == 'byr':
        value = int(value)
        if (1920 <= value) and (value <= 2002):
            return True
        else:
            return False
    elif key == 'iyr':
        value = int(value)
        if (2010 <= value) and (value <= 2020):
            return True
        else:
            return False
    elif key == 'eyr':
        value = int(value)
        if (2020 <= value) and (value <= 2030):
            return True
        else:
            return False
    elif key == 'hgt':
        measure = int(value[:-2])
        metric = value[-2:]
        if (metric == 'in') and ((59 <= measure) and (measure <= 76)):
            return True
        elif (metric == 'cm') and ((150 <= measure) and (measure <= 193)):
            return True
        else:
            return False
    elif key == 'hcl':
        pattern = re.compile("^#[a-f0-9]{6}$")
        match =  pattern.match(value)
        return bool(match)
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        pattern = re.compile("^[0-9]{9}$")
        match =  pattern.match(value)
        return bool(match)
    else:
        return True

valid_passports_p2 = 0
current_passport = dict()

for index, line in enumerate(passports):
    if line == '':
        all_valid = all(is_valid(item) for item in current_passport.items())
        all_mandatory = all(key in current_passport.keys() for key in mandatory_keys)
        if all_mandatory and all_valid:
            valid_passports_p2 += 1
        current_passport = dict()
    else:
        elements = line.split()
        for element in elements:
            key = element.split(':')[0]
            value = element.split(':')[1]
            current_passport[key] = value

    if index == (len(passports) - 1):
        all_valid = all(is_valid(item) for item in current_passport.items())
        all_mandatory = all(key in current_passport.keys() for key in mandatory_keys)
        if all_mandatory and all_valid:
            valid_passports_p2 += 1

print("Part 2 Answer:", valid_passports_p2)
