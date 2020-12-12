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

instructions = get_clean_data()

# Part 1

def move_coords(position, command, argument):
    if command == 'N': # move north arg number of positions (y-axis, positive)
        position[1] += argument
    elif command == 'S': # move south arg number of positions (y-axis, negative)
        position[1] -= argument
    elif command == 'E': # move east arg number of positions (x-axis, positive)
        position[0] += argument
    elif command == 'W': # move west arg number of positions (x-axis, negative)
        position[0] -= argument
    return position

def rotate_direction(direction, command, rotation):
    sequence = ['N', 'E', 'S', 'W']
    direction_index = sequence.index(direction)
    rotation_steps = int(rotation / 90)
    
    if command == 'R':
        new_direction_index = (direction_index + rotation_steps) % len(sequence)
    elif command == 'L':
        new_direction_index = (direction_index - rotation_steps) % len(sequence)
        
    return sequence[new_direction_index]

def navigate(instructions):
    position = [0, 0]
    direction = 'E'

    for instruction in instructions:
        command, argument = instruction[:1], int(instruction[1:])
        # print("Location: ({}, {}); Direction: {}".format(position[0], position[1], direction))
        # print("Command: {} {}".format(command, argument))
        if command in ['L', 'R']: # rotate left or right arg number of degrees (multiples of 90)
            direction = rotate_direction(direction, command, argument)
        elif command == 'F': # move forward arg number of positions
            position = move_coords(position, direction, argument)
        elif command in ['N', 'S', 'E', 'W']:
            position = move_coords(position, command, argument)
        # print("Result - Location: ({}, {}); Direction: {}".format(position[0], position[1], direction))
    return position

def part_one_answer(instructions):
    position = navigate(instructions)
    manhatan_dist = sum([abs(item) for item in position])
    print("Ship Location: ({},{})".format(position[0], position[1]))
    print("Part 1 Answer: {}".format(manhatan_dist))
    
part_one_answer(instructions)


# Part 2

def rotate_waypoint(waypoint, command, argument):
    import math
    
    if command == 'R':
        argument = (-argument) % 360
    
    radians = math.radians(argument)
    new_x = waypoint[0] * math.cos(radians) - waypoint[1] * math.sin(radians)
    new_x = int(round(new_x))
    
    new_y = waypoint[0] * math.sin(radians) + waypoint[1] * math.cos(radians)
    new_y = int(round(new_y))
        
    return [new_x, new_y]

def new_navigate(instructions):
    ship = [0, 0]
    waypoint = [10, 1]

    for instruction in instructions:
        command, argument = instruction[:1], int(instruction[1:])
        # print("Location: ({}, {}); Waypoint: ({}, {})".format(ship[0], ship[1], waypoint[0], waypoint[1]))
        # print("Command: {} {}".format(command, argument))
        if command in ['L', 'R']: # rotate the waypoint left or right arg number of degrees (multiples of 90)
            waypoint = rotate_waypoint(waypoint, command, argument)
        elif command == 'F': # move the ship to the waypoint x number of times
            ship = [ship_coord + waypoint_coord * argument for ship_coord, waypoint_coord in zip(ship, waypoint)]
        elif command in ['N', 'S', 'E', 'W']:
            waypoint = move_coords(waypoint, command, argument) # move waypoint as specified in command
        # print("Result - Location: ({}, {}); Waypoint: ({}, {})".format(ship[0], ship[1], waypoint[0], waypoint[1]), end="\n\n")
    return ship

def part_two_answer(instructions):
    ship_position = new_navigate(instructions)
    manhattan_distance = sum([abs(item) for item in ship_position])
    print("Ship Location: ({},{})".format(ship_position[0], ship_position[1]))
    print("Part 2 Answer: {}".format(manhattan_distance))
    
part_two_answer(instructions)