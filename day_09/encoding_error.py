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

number_list = get_clean_data()
number_list = [int(item) for item in number_list]

# Part 1

def is_valid(number, num_list):
    found = False
    for item in num_list:
        diff = number - item
        temp_list = num_list[:]
        temp_list.remove(item)
        if diff in temp_list:
            found = True
            break
    return found

index = 25
valid_value = True
invalid_number = None

while valid_value:
    min_range = index - 25
    check_range = number_list[min_range:index]
    valid_value = is_valid(number_list[index], check_range)
    
    if valid_value:
        index += 1
    else:
        invalid_number = number_list[index]

print("Part 1 Answer:", invalid_number)

# Part 2

start_index = 0
sum_equals_value = False
sum_list = []

while not sum_equals_value:
    num_sum = number_list[start_index]
    current_index = start_index
    while num_sum < invalid_number:
        current_index += 1
        num_sum += number_list[current_index]
    
    if num_sum == invalid_number:
        sum_equals_value = True
        sum_list = number_list[start_index:(current_index + 1)]
    elif num_sum > invalid_number:
        start_index += 1

min_number = min(sum_list)
max_number = max(sum_list)
print("Part 2 Answer:", min_number + max_number)