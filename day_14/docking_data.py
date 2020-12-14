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

data = get_clean_data()

# Part 1

def parse_row(row):
    name, value = [item.strip() for item in row.split('=')]
    return name, value

def get_memory_location(mem):
    location = mem.split('[')[1].split(']')[0]
    return int(location)

def mask_value(mask, bin_value):
    masked_val = ''
    binary_length = len(mask)
    length_difference = binary_length - len(bin_value)
    full_bin_value = '0' * length_difference + bin_value
    for mask_item, bin_item in zip(mask, full_bin_value):
        if mask_item != 'X':
            masked_val += mask_item
        else:
            masked_val += bin_item
    return masked_val

def run_program(data):
    mem_dict = dict()
    _, mask = parse_row(data[0])
    for index in range(1, len(data)):
        name, value = parse_row(data[index])
        if name == 'mask':
            mask = value
        else:
            bin_value = bin(int(value))[2:] # remove '0b' prefix
            new_value = mask_value(mask, bin_value)
            location = get_memory_location(name)
            mem_dict[location] = int(new_value, 2)
    return mem_dict

memory_p1 = run_program(data)
print("Part 1 Answer: {}".format(sum(memory_p1.values())))


# Part 2

def mask_address(mask, bin_value):
    masked_val = ''
    binary_length = len(mask)
    length_difference = binary_length - len(bin_value)
    full_bin_value = '0' * length_difference + bin_value
    for mask_item, bin_item in zip(mask, full_bin_value):
        if mask_item in ['1', 'X']:
            masked_val += mask_item
        elif mask_item == '0':
            masked_val += bin_item
    return masked_val

def generate_locations(template):
    import itertools
    
    templates = []
    binary_elements = ['0', '1']
    combination_count = template.count('X')
    
    combinations = list(itertools.product(binary_elements, repeat=combination_count))
    
    for combination in combinations:
        temp_address = ''
        
        combination_index = 0
        for character in template:
            if character != 'X':
                temp_address += character
            else:
                temp_address += combination[combination_index]
                combination_index += 1
        
        templates.append(temp_address)
    
    return templates

def run_program_v2(data):
    mem_dict = dict()
    _, mask = parse_row(data[0])
    for index in range(1, len(data)):
        name, value = parse_row(data[index])
        if name == 'mask':
            mask = value
        else:
            location = get_memory_location(name)
            bin_location = bin(int(location))[2:] # remove '0b' prefix
            template_location = mask_address(mask, bin_location)
            locations = generate_locations(template_location)
            
            value = int(value)
            for location in locations:
                int_location = int(location, 2)
                mem_dict[location] = value
            
    return mem_dict

memory_p2 = run_program_v2(data)
print("Part 2 Answer: {}".format(sum(memory_p2.values())))