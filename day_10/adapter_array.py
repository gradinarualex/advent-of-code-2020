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

adapter_jolts = get_clean_data() # read data in
adapter_jolts = [int(item) for item in adapter_jolts] # convert values from string to int
adapter_jolts.append(0) # append the outlet jolt value
sorted_jolts = sorted(adapter_jolts) # sort values in increasing order

# Part 1

# create an empty dictionary to store the count for each difference
difference_dict = dict()

for index in range(len(sorted_jolts) - 1):
    difference = sorted_jolts[index + 1] - sorted_jolts[index]
    if difference in difference_dict:
        difference_dict[difference] += 1
    else:
        difference_dict[difference] = 1

# inser difference between the last adapter and device (3 jolts)
device_difference = 3
difference_dict[device_difference] += 1

p1_answer = difference_dict[1] * difference_dict[3]
print("Part 1 Answer:", p1_answer)

# Part 2

position_steps = dict()
def count_steps(position):
    # if this is the last step return 1
    if position == len(sorted_jolts) - 1:
        return 1
    # if position steps already exists, return that number
    if position in position_steps:
        return position_steps[position]
    
    # the count of all possible ways to reach the end is the sum
    # of all ways to reach the previous steps, if within 3 jolts
    count = 0
    for ulterior_position in range(position + 1, len(sorted_jolts)):
        if sorted_jolts[ulterior_position] - sorted_jolts[position] <= 3:
            count += count_steps(ulterior_position)
    
    position_steps[position] = count
    return count

p2_answer = count_steps(0) # start count from first position to get answer
print("Part 2 Answer:", p2_answer)
