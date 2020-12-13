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

schedules = get_clean_data()

# Part 1

timestamp = int(schedules[0])
shuttles = [int(item) for item in schedules[1].split(',') if item != 'x'] # get each shuttle name as int and remove all out of service shuttles

min_wait = max(shuttles) # initialize minimum waiting time with the longest shuttle time
earliest_shuttle = None

for shuttle in shuttles:
    wait_time = shuttle - (timestamp % shuttle)
    if wait_time < min_wait:
        min_wait = wait_time
        earliest_shuttle = shuttle

print("Part 1 Answer: {}".format(min_wait * earliest_shuttle))

# Part 2

shuttles = schedules[1].split(',') # get each shuttle name

def earliest_time(shuttle_list):
    earliest_time = 0
    multiplier = 1

    # implementation of the chinese remainder theorem
    # took a lot to figure out 1/ that this is what i should apply and 2/ how to reverse engineer for this problem
    # link to an algorithm walkthrough: https://www.youtube.com/watch?v=zIFehsBHB8o
    for index, shuttle in enumerate(shuttle_list):
        if shuttle != 'x':
            shuttle_int = int(shuttle)
            while ((earliest_time + index) % shuttle_int) != 0:
                earliest_time += multiplier
            multiplier *= shuttle_int
            
    return earliest_time

print("Part 2 Answer: {}".format(earliest_time(shuttles)))