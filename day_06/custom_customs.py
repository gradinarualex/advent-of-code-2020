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

answers = get_clean_data()

# Part 1

unique_answers = 0
group_answers = []

for index, line in enumerate(answers):
    if line == '':
        # group_members = len(group_answers)
        all_answers = ''.join(group_answers)
        unique_group_answers = len(set(all_answers))
        unique_answers += unique_group_answers

        group_answers = []
    else:
        group_answers.append(line)

    if index == (len(answers) - 1):
        all_answers = ''.join(group_answers)
        unique_group_answers = len(set(all_answers))
        unique_answers += unique_group_answers

print("Part 1 Answer:", unique_answers)


# Part 2

unanimous_answers = 0
group_common = None

for index, line in enumerate(answers):
    if line == '':
        unanimous_answers += len(group_common)
        group_common = None
    else:
        passenger_answers = [char for char in line]
        if group_common == None:
            group_common = passenger_answers
        else:
            group_common = [answer for answer in passenger_answers if answer in group_common]

    if index == (len(answers) - 1):
        unanimous_answers += len(group_common)

print("Part 2 Answer:", unanimous_answers)
