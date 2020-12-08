# Define function that reads and processes input file (clean newline from each row)
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

# Read in the data
geomap = get_clean_data()

# Set challenge variables
tree_sym = '#'
cols = len(geomap[0])
rows = len(geomap)

# Define function that gets the number of trees encountered based on the slope provided
def get_trees_encountered(slope):
    # slope is expected to be a tuple with number of moves to the right (col_moves) and then moves down (row_moves)
    col_moves, row_moves = slope

    curr_row = 0
    curr_col = 0

    trees_encountered = 0
    while curr_row < (rows - 1):
        curr_row += row_moves
        curr_col = (curr_col + col_moves) % cols

        if geomap[curr_row][curr_col] == tree_sym:
            trees_encountered += 1

    return trees_encountered

# Part 1 - Result
slope = (3, 1) # 3 moves to the right, 1 move down
p1_result = get_trees_encountered(slope)
print("Part 1 Answer: ", p1_result)

# Part 2 - Result
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

trees_encountered_list = []
p2_result = 1
for slope in slopes:
    trees_encountered = get_trees_encountered(slope)
    trees_encountered_list.append(trees_encountered)
    p2_result *= trees_encountered

print("Part 2 Answer:", p2_result)
