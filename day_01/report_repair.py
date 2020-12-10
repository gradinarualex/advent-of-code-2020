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

report = get_clean_data() # read data in
report = [int(item) for item in report] # convert elements to int

target = 2020

# find pair of numbers adding up to 2020
for item in report:
    difference = target - item
    if difference in report:
        print("Part 1 Answer: {} * {} = {}".format(item, difference, item * difference))
        break


# find triplet of numbers adding up to 2020
found = False
for i in report:
    for j in report:
        if i + j < target:
            difference = target - (i + j)
            if difference in report:
                print("Part 2 Answer: {} * {} * {} = {}".format(i, j, difference, i * j * difference))
                found = True
                break
        if found:
            break
