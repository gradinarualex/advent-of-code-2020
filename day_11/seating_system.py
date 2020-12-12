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

seat_layout = get_clean_data()

# Part 1

def count_occupied(layout):
    count_occupied = 0
    for row_id in range(len(layout)):
        for col_id in range(len(layout[0])):
            if layout[row_id][col_id] == '#':
                count_occupied +=1
    return count_occupied

def generate_adjacent_indexes(array=seat_layout, position=(0,0)):
    row, col = position
    
    adjacent_seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            current_row = row + i
            current_col = col + j
            
            not_self = not ((i==0) and (j==0))
            row_in_array = (current_row >= 0) and (current_row < len(array))
            col_in_array = (current_col >= 0) and (current_col < len(array[0]))
            
            if not_self and row_in_array and col_in_array:
                adj_seat = (current_row, current_col)
                adjacent_seats.append(adj_seat)
    return adjacent_seats

def get_adjacent_occupied(array=seat_layout, position=(0, 0)):
    row, col = position
    adjacent_seats = generate_adjacent_indexes(array, position)
    
    occupied = 0
    for seat in adjacent_seats:
        check_row, check_col = seat
        seat_status = array[check_row][check_col]
        if seat_status == '#':
            occupied += 1
    
    return occupied

def occupy_seats(layout):
    new_layout = layout[:] # copy array
    
    free = 'L'
    occupied = '#'
    
    row_length = len(layout)
    col_length = len(layout[0])
    
    for row_index in range(row_length):
        for col_index in range(col_length):
            seat = layout[row_index][col_index]
            adjacent_occupied = get_adjacent_occupied(layout, (row_index, col_index))
            
            if seat == free and adjacent_occupied == 0:
                seats_row = new_layout[row_index]
                new_row = seats_row[:col_index] + occupied + seats_row[col_index + 1:]
                new_layout[row_index] = new_row
                # check if any! seats around occupied. if not - occupy
            elif seat == occupied and adjacent_occupied >= 4:
                seats_row = new_layout[row_index]
                new_row = seats_row[:col_index] + free + seats_row[col_index + 1:]
                new_layout[row_index] = new_row
                # check if >=4 seats arround are occupied. if so - free seat
    
    return new_layout

def occupy_adjacent_iterate(layout):
    current_layout = layout[:]
    while True:
        new_layout = occupy_seats(current_layout)
        if new_layout == current_layout:
            return new_layout[:]
        else:
            current_layout = new_layout[:]

layout_p1 = occupy_adjacent_iterate(seat_layout)
seat_count_p1 = count_occupied(layout_p1)
print("Part 1 Answer:", seat_count_p1)            


# Part 2

def generate_directional_indexes(array=seat_layout, position=(0,0)):
    row, col = position
    
    adjacent_seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            
            current_row = row + i
            current_col = col + j

            row_in_array = (current_row >= 0) and (current_row < len(array))
            col_in_array = (current_col >= 0) and (current_col < len(array[0]))
            
            if not (row_in_array and col_in_array):
                continue
            else:
                direction_empty = False
                while array[current_row][current_col] == '.':
                    next_row_in_array = (current_row + i >= 0) and (current_row + i < len(array))
                    next_col_in_array = (current_col + j >= 0) and (current_col + j < len(array[0]))
                    if next_row_in_array and next_col_in_array:
                        current_row = current_row + i
                        current_col = current_col + j
                    else:
                        direction_empty = True
                        break
                
                if direction_empty:
                    continue
                else:
                    adj_seat = (current_row, current_col)
                    adjacent_seats.append(adj_seat)
    return adjacent_seats

def get_directional_occupied(array=seat_layout, position=(0, 0)):
    row, col = position
    adjacent_seats = generate_directional_indexes(array, position)
    
    occupied = 0
    for seat in adjacent_seats:
        check_row, check_col = seat
        seat_status = array[check_row][check_col]
        if seat_status == '#':
            occupied += 1
    
    return occupied

def occupy_directional_seats(layout):
    new_layout = layout[:] # copy array
    
    free = 'L'
    occupied = '#'
    
    row_length = len(layout)
    col_length = len(layout[0])
    
    for row_index in range(row_length):
        for col_index in range(col_length):
            # print("({},{})".format(row_index, col_index))
            seat = layout[row_index][col_index]
            if seat != '.':
                directional_occupied = get_directional_occupied(layout, (row_index, col_index))
            
                if seat == free and directional_occupied == 0:
                    seats_row = new_layout[row_index]
                    new_row = seats_row[:col_index] + occupied + seats_row[col_index + 1:]
                    new_layout[row_index] = new_row
                    # check if any! seats around occupied. if not - occupy
                elif seat == occupied and directional_occupied >= 5:
                    seats_row = new_layout[row_index]
                    new_row = seats_row[:col_index] + free + seats_row[col_index + 1:]
                    new_layout[row_index] = new_row
                    # check if >=5 seats arround are occupied. if so - free seat
    
    return new_layout

def occupy_directional_iterate(layout):
    current_layout = layout[:]
    while True:
        new_layout = occupy_directional_seats(current_layout)
        if new_layout == current_layout:
            return new_layout[:]
        else:
            current_layout = new_layout[:]

layout_p2 = occupy_directional_iterate(seat_layout)
seat_count_p2 = count_occupied(layout_p2)
print("Part 2 Answer:", seat_count_p2)