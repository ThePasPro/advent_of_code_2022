data = open('day_02_input.txt').read().splitlines()

score = 0
for game in data:
    opponent_turn, my_turn = game.split()

    if my_turn == 'X':
        score += 1
    elif my_turn == 'Y':
        score += 2
    elif my_turn == 'Z':
        score += 3

    if opponent_turn == 'A':
        if my_turn == 'X':
            score += 3
        elif my_turn == 'Y':
            score += 6
        else:
            score += 0

    elif opponent_turn == 'B':
        if my_turn == 'Y':
            score += 3
        elif my_turn == 'Z':
            score += 6
        else:
            score += 0

    elif opponent_turn == 'C':
        if my_turn == 'Z':
            score += 3
        elif my_turn == 'X':
            score += 6
        else:
            score += 0

print(score)