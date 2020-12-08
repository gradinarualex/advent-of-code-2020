import os

# get input file path
file_path = os.path.join(os.getcwd(), 'input.txt')

# read input file data as list of lines
with open(file_path) as f:
    report = f.readlines()

# clean lines - remove new line character and convert to integer
report = [int(item.replace('\n','')) for item in report]

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
