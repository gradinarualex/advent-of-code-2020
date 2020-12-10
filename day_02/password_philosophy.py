import os

# Define function that reads and processes input file (clean newline from each row)
def get_clean_data():
    import os

    # get input file path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'input.txt')

    # read input file data as list of lines
    with open(file_path) as f:
        lines = f.readlines()

    # clean lines - remove new line character
    lines = [line.replace('\n','') for line in lines]

    return lines

logs = get_clean_data() # read data in

## Part 1

# splits line into elements for easier processing
def get_elements(log):
    specs = log.split(':')[0]
    password = log.split(':')[1].strip()

    character = specs.split()[1]
    limits = specs.split()[0]

    min_limit = int(limits.split('-')[0])
    max_limit = int(limits.split('-')[1])

    return (min_limit, max_limit, character, password)

# set validation counter to 0
validation_counter_p1 = 0

for log in logs:
    # get individual elements
    min_lim, max_lim, char, passwd = get_elements(log)

    # set a char counter to zero
    char_counter = 0
    for ch in passwd:
        if ch == char:
            char_counter += 1

    # if char occurances between min and max limits, increment validation counter
    if (min_lim <= char_counter) and (char_counter <= max_lim):
        validation_counter_p1 += 1

print("Part 1 Answer:", validation_counter_p1)

## Part 2

validation_counter_p2 = 0

for log in logs:
    first_index, second_index, char, passwd = get_elements(log)

    first_index = first_index - 1
    second_index = second_index - 1

    if (passwd[first_index] == char) != (passwd[second_index] == char):
        validation_counter_p2 += 1

print("Part 2 Answer:", validation_counter_p2)
