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

def calculate(equation):
    stripped_equation = equation.replace(' ', '')
    
    subtotal = 0
    operator = '+'
    
    index = 0
    while index < len(stripped_equation):
        elem = stripped_equation[index]
        if elem == '(':
            disparity = 1
            starting_index = index
            while disparity != 0:
                # print(index)
                index += 1
                if stripped_equation[index] == '(':
                    disparity += 1
                if stripped_equation[index] == ')':
                    disparity -= 1
                    
            value = calculate(stripped_equation[(starting_index + 1):index])
            if operator == '+':
                subtotal += value
            elif operator == '*':
                subtotal *= value
        elif elem == '*':
            operator = '*'
        elif elem == '+':
            operator = '+'
        else:
            value = int(elem)
            if operator == '+':
                subtotal += value
            elif operator == '*':
                subtotal *= value
        
        index += 1
    
    return subtotal
    
def part_one():
    equations = get_clean_data()
    values_sum = 0
    
    for equation in equations:
        values_sum += calculate(equation)
        
    return values_sum

print("Part 1 Answer: {}".format(part_one()))


# Part 2

def calculate_p2(equation):
    stripped_equation = equation.replace(' ', '')
    
    total = 0
    value = None
    operator = None
    
    index = 0
    previous_value = None
    previous_operator = None
    
    while index < len(stripped_equation):
        
        elem = stripped_equation[index]
        if elem == '(':
            disparity = 1
            starting_index = index
            while disparity != 0:
                index += 1
                if stripped_equation[index] == '(':
                    disparity += 1
                if stripped_equation[index] == ')':
                    disparity -= 1
            elem = calculate_p2(stripped_equation[(starting_index + 1):index])
        
        if elem in ['+', '*']:
            operator = elem
        elif elem != ')':
            value = int(elem)
            if previous_value == None:
                if operator != '*':
                    total += value
                elif operator == '*':
                    previous_value = value
                    previous_operator = operator
            elif previous_operator == None:
                if operator == '+':
                    total += value
                    previous_value = None
                    previous_operator = None
                elif operator == '*':
                    previous_value = value
                    previous_operator = operator
            elif previous_operator == operator:
                if operator == '*':
                    total *= previous_value
                    previous_value = value
                    previous_operator = '*'
                elif operator == '+':
                    total += previous_value
                    previous_value = None
                    previous_operator = None
            elif previous_operator == '*':
                previous_value += value # operator is +
            elif previous_operator == '+':
                total += previous_value # operator is *
                previous_value = value
             
        index += 1
    
    if previous_value != None:
        if previous_operator == '*':
            total *= previous_value
    
    return total
    
def part_two():
    equations = get_clean_data()
    values_sum = 0
    
    for equation in equations:
        values_sum += calculate_p2(equation)
        
    return values_sum

print("Part 2 Answer: {}".format(part_two()))