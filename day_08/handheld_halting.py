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

boot_instructions = get_clean_data()

# Part 1

def calc_accumulator(boot_instructions):
    accumulator = 0
    index = 0

    visited_indexes = []

    while (index not in visited_indexes) and (index < len(boot_instructions)):
        command = boot_instructions[index]
        operation, argument = command.split()
        argument = int(argument)

        visited_indexes.append(index)

        if operation == 'acc':
            accumulator += argument
            index += 1
        elif operation == 'nop':
            index += 1
        elif operation == 'jmp':
            index += argument
        else:
            print("Invalid operation at line ", index, ". Halting execution.", sep="")
            break

    return accumulator, visited_indexes

accumulator_p1, log_trace = calc_accumulator(boot_instructions)

print("Part 1 Answer:", accumulator_p1)


# Part 2

# check if booting finishes (True if finishes, false if not)
def is_booting(instructions):
    index = 0
    visited_indexes = []

    is_looping = False
    while (not is_looping) and (index < len(instructions)):
        command = instructions[index]
        operation, argument = command.split()
        argument = int(argument)

        visited_indexes.append(index)

        if operation == 'acc':
            index += 1
        elif operation == 'nop':
            index += 1
        elif operation == 'jmp':
            index += argument
        else:
            print("Invalid operation at line ", index, ". Halting execution.", sep="")
            break
            
        if index in visited_indexes:
            is_looping = True
    
    if is_looping:
        return False
    else:
        return True

max_pos = max(log_trace)
max_pos_index = log_trace.index(max_pos)

corrected_boot_instructions = []
current_pos_index = max_pos_index

while True:
    boot_index = log_trace[current_pos_index]
    boot_instruction = boot_instructions[boot_index]
    operation, argument = boot_instruction.split()
    
    if operation == 'jmp':
        new_command = ' '.join(['nop', argument])
    elif operation == 'nop':
        new_command = ' '.join(['jmp', argument])
        
    changed_boot_instructions = boot_instructions[:]
    changed_boot_instructions[boot_index] = new_command
    
    booted = is_booting(changed_boot_instructions)
    
    if booted:
        corrected_boot_instructions = changed_boot_instructions
        break
    else:
        current_pos_index -= 1
        
accumulator_p2, _ = calc_accumulator(corrected_boot_instructions)

print("Part 2 Answer:", accumulator_p2)