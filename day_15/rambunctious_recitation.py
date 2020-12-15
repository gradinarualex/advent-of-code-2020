game_start = [6, 4, 12, 1, 20, 0, 16]

# Part 1

def play_game(game_start, turns):
    iter_count = 0
    
    number_occurances = dict()
    game_history = game_start[:-1]
    
    for number in game_history:
        number_occurances[number] = iter_count
        latest_item = number
        iter_count += 1
    
    next_item = game_start[-1]
    
    while iter_count < turns:
        # case if latest_item has been spoken before
        if next_item in number_occurances:
            new_item = iter_count - number_occurances[next_item]
            number_occurances[next_item] = iter_count
            game_history.append(next_item)
            next_item = new_item
            iter_count += 1
        # case if latest_item is first time spoken
        else:
            number_occurances[next_item] = iter_count
            game_history.append(next_item)
            next_item = 0
            iter_count += 1
    
    return game_history

game_history = play_game(game_start, 2020)
p1_answer = game_history[-1]
print("Part 1 Answer:", p1_answer)

# Part 2

game_history = play_game(game_start, 30000000)
p2_answer = game_history[-1]
print("Part 2 Answer:", p2_answer)