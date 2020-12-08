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

luggage_rules = get_clean_data()

# Part 1

target_bags = ['shiny gold']

all_target_bags = []
while True:
    new_targets=[]
    for rule in luggage_rules:
        container, contained = rule.split('contain')
        target_found = False
        for target_bag in target_bags:
            if target_bag in contained:
                target_found = True
    
        if target_found:
            new_target = ' '.join(container.split()[:2])
            new_targets.append(new_target)

    all_target_bags.extend(new_targets)
    
    if new_targets != []:
        target_bags = new_targets
    else:
        break
        
unique_bags = len(set(all_target_bags))
print("Part 1 Answer:", unique_bags)


# Part 2

def get_count_and_name(item):
    if 'no' in item:
        return 0, 'none'
    else:
        item_split = item.split()
        item_count = int(item_split[0])
    
        new_container = ' '.join(item_split[1:3])
    
        return item_count, new_container

def get_bag_count_recursive(search_item):    
    rule_index = None
    for index, rule in enumerate(luggage_rules):
        container, contained = rule.split('contain')
        if search_item in container:
            rule_index = index
    
    container, contained = luggage_rules[rule_index].split('contain')
    contained_items = [item.strip() for item in contained.split(',')]
    
    bag_count = 0
    for item in contained_items:
        item_count, item_name = get_count_and_name(item)
        if item_count != 0:
            bag_count += item_count + item_count * get_bag_count_recursive(item_name)
        
    return bag_count

starting_bag = 'shiny gold'
part_2_answer = get_bag_count_recursive(starting_bag)
print("Part 2 Answer:", part_2_answer)