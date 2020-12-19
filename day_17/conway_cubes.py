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

# Part 1

def set_structure_3d(setup):
    z = 0

    space = dict()
    for y, row in enumerate(setup):
        for x, char in enumerate(row):
            key = (z, y, x)
            if char == '#':
                space[key] = True
            elif char == '.':
                space[key] = False

    return space

def get_neighbors_3d(coords):
    z, y, x = coords
    neighbor_offsets = [-1, 0, 1]

    neighbor_list = []
    for z_offset in neighbor_offsets:
        z_idx = z + z_offset
        for y_offset in neighbor_offsets:
            y_idx = y + y_offset
            for x_offset in neighbor_offsets:
                x_idx = x + x_offset
                if not (z_offset == y_offset == x_offset == 0):
                    neighbor = (z_idx, y_idx, x_idx)
                    neighbor_list.append(neighbor)

    return neighbor_list

def count_neighbors(space, neighbors):
    neighbors_count = 0

    for neighbor in neighbors:
        if neighbor in space:
            if space[neighbor] == True:
                neighbors_count += 1

    return neighbors_count

def expand_space_3d(space):
    new_space = space.copy()

    for cube in space.keys():
        neighbors = get_neighbors_3d(cube)
        for neighbor in neighbors:
            if not (neighbor in space.keys()):
                new_space[neighbor] = False

    return new_space

def next_state_3d(space):

    new_space = space.copy()

    # expand space
    new_space = expand_space_3d(new_space)

    # make changes based on rules
    for cube in new_space.keys():
        neighbors = get_neighbors_3d(cube)
        neighbors_count = count_neighbors(space, neighbors)

        if (new_space[cube] == True) and (neighbors_count not in [2, 3]):
            new_space[cube] = False
        elif (new_space[cube] == False) and (neighbors_count == 3):
            new_space[cube] = True

    return new_space

def count_cubes(space):
    count = 0
    for cube in space:
        if space[cube] == True:
            count += 1

    return count

def run_conway_cubes_3d(space, cycles=6):
    for _ in range(cycles):
        space = next_state_3d(space)

    return count_cubes(space)

setup = get_clean_data()
space = set_structure_3d(setup)
p1_answer = run_conway_cubes_3d(space)
print("Part 1 Answer: {}".format(p1_answer))


# Part 2

def set_structure_4d(setup):
    t = 0
    z = 0

    space = dict()
    for y, row in enumerate(setup):
        for x, char in enumerate(row):
            key = (t, z, y, x)
            if char == '#':
                space[key] = True
            elif char == '.':
                space[key] = False

    return space

def get_neighbors_4d(coords):
    t, z, y, x = coords
    neighbor_offsets = [-1, 0, 1]

    neighbor_list = []
    for t_offset in neighbor_offsets:
        t_idx = t + t_offset
        for z_offset in neighbor_offsets:
            z_idx = z + z_offset
            for y_offset in neighbor_offsets:
                y_idx = y + y_offset
                for x_offset in neighbor_offsets:
                    x_idx = x + x_offset
                    if not (t_offset == z_offset == y_offset == x_offset == 0):
                        neighbor = (t_idx, z_idx, y_idx, x_idx)
                        neighbor_list.append(neighbor)

    return neighbor_list

def expand_space_4d(space):
    new_space = space.copy()

    for cube in space.keys():
        neighbors = get_neighbors_4d(cube)
        for neighbor in neighbors:
            if not (neighbor in space.keys()):
                new_space[neighbor] = False

    return new_space

def next_state_4d(space):

    new_space = space.copy()

    # expand space
    new_space = expand_space_4d(new_space)

    # make changes based on rules
    for cube in new_space.keys():
        neighbors = get_neighbors_4d(cube)
        neighbors_count = count_neighbors(space, neighbors)

        if (new_space[cube] == True) and (neighbors_count not in [2, 3]):
            new_space[cube] = False
        elif (new_space[cube] == False) and (neighbors_count == 3):
            new_space[cube] = True

    return new_space

def run_conway_cubes_4d(space, cycles=6):
    for _ in range(cycles):
        space = next_state_4d(space)

    return count_cubes(space)

space = set_structure_4d(setup)
p2_answer = run_conway_cubes_4d(space)
print("Part 2 Answer: {}".format(p2_answer))
