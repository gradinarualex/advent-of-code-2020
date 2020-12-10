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

seat_locations = get_clean_data()

# Part 1

def parse_seat(sequence):
    min_row = 0
    max_row = 127

    row_seq = sequence[:-3]
    for elem in row_seq:
        if elem == 'F':
            max_row = int((min_row + max_row) / 2)
        elif elem == 'B':
            min_row = int((min_row + max_row + 1) / 2)

    min_col = 0
    max_col = 7

    col_seq = sequence[-3:]

    for elem in col_seq:
        if elem == 'L':
            max_col = int((min_col + max_col) / 2)
        elif elem == 'R':
            min_col = int((min_col + max_col + 1 ) / 2)

    return (max_row, max_col)

seat_ids = []
for seat in seat_locations:
    row, col = parse_seat(seat)
    seat_id = row * 8 + col
    seat_ids.append(seat_id)

print('Part 1 Answer:', max(seat_ids))


# Part 2

your_seat = None
sorted_seats = sorted(seat_ids)
for index in range(len(seat_ids) - 1):
    if (sorted_seats[index + 1] - sorted_seats[index]) == 2:
        your_seat = int((sorted_seats[index + 1] + sorted_seats[index]) / 2)
        break

print('Part 2 Answer:', your_seat)
