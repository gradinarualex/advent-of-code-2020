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

ticket_data = get_clean_data()
rules = ticket_data[:20]
my_ticket = ticket_data[22]
nearby_tickets = ticket_data[25:]

def get_restrictions(rules):
    restrictions = []
    for rule in rules:
        ranges = rule.split(':')[1].strip()
        range_list = [item.strip() for item in ranges.split('or')]
        for range_item in range_list:
            range_limits = [int(item) for item in range_item.split('-')]
            range_set = (range_limits[0], range_limits[1])
            restrictions.append(range_set)
    return restrictions

def validate_tickets(tickets):
    restriction_rules = get_restrictions(rules)

    scanning_errors = 0
    for ticket in tickets:
        fields = [int(item.strip()) for item in ticket.split(',')]
        
        for field in fields:
            count_invalid = 0
            for restriction in restriction_rules:
                if field < restriction[0] or field > restriction[1]:
                    count_invalid += 1
            if count_invalid == len(restriction_rules):
                scanning_errors += field

    return scanning_errors

p1_answer = validate_tickets(nearby_tickets)
print("Part 1 Answer: {}".format(p1_answer))


# Part 2

def discard_tickets(tickets):
    restriction_rules = get_restrictions(rules)
    new_tickets = []

    for ticket in tickets:
        fields = [int(item) for item in ticket.split(',')]
        
        ticket_valid = True
        for field in fields:
            count_invalid = 0
            for restriction in restriction_rules:
                if not (restriction[0] <= field and field <= restriction[1]):
                    count_invalid += 1
            if count_invalid == len(restriction_rules):
                ticket_valid = False
                break
        
        if ticket_valid:
            new_tickets.append(ticket)

    return new_tickets

def split_tickets(tickets):
    new_tickets = tickets[:]
    for index, row in enumerate(new_tickets):
        new_row = [int(item) for item in row.split(',')]
        new_tickets[index] = new_row
    
    return new_tickets

def structure_rules(rules):
    field_rules = dict()
    for rule in rules:
        rule_elems = [item.strip() for item in rule.split(':')]
        field = rule_elems[0]
        ranges = rule_elems[1]
        range_list = [item.strip() for item in ranges.split('or')]
        
        rules_list = []
        for range_item in range_list:
            range_limits = [int(item) for item in range_item.split('-')]
            range_set = (range_limits[0], range_limits[1])
            rules_list.append(range_set)
        
        field_rules[field] = rules_list
        
    return field_rules

def check_eligibility(rules, nearby_tickets):
    clean_tickets = discard_tickets(nearby_tickets)
    clean_split_tickets = split_tickets(clean_tickets)
    rules_dict = structure_rules(rules)
    
    n_cols = len(clean_split_tickets[0])
    
    col_field_eligibility = dict()
    for col_idx in range(n_cols):
        possible_fields = [field for field in list(rules_dict.keys())]
        
        fields_list = []
        for possible_field in possible_fields:
            valid_field = True
            field_rules = rules_dict[possible_field]
            
            values = [item[col_idx] for item in clean_split_tickets]
            for value in values:                
                any_rules = False
                for field_rule in field_rules:
                    any_rules = (any_rules or (field_rule[0] <= value) and (value <= field_rule[1]))
                
                if not any_rules:
                    valid_field = False
                    break
            
            if valid_field:
                fields_list.append(possible_field)
                
        col_field_eligibility[col_idx] = fields_list
    
    return col_field_eligibility

def resolve_fields(eligibility_dictionary):
    eligibility_dict = eligibility_dictionary.copy()
    
    fields_list = [0] * len(eligibility_dict)

    for i in range(len(eligibility_dict)):
        found_field = None
        found_index = None

        for index, fields in eligibility_dict.items():
            if len(fields) == 1:
                fields_list[index] = fields[0]
                found_field = fields[0]
                del eligibility_dict[index]
                break

        for index, fields in eligibility_dict.items():
            if found_field in fields:
                fields.remove(found_field)
                eligibility_dict[index] = fields

    return fields_list

eligibility_dict = check_eligibility(rules, nearby_tickets)
fields_list = resolve_fields(eligibility_dict)

my_ticket_list = [int(item) for item in my_ticket.split(',')]

p2_answer = 1
for field, value in zip(fields_list, my_ticket_list):
    if 'departure' in field:
        p2_answer *= value 
        
print("Part 2 Answer: {}".format(p2_answer))