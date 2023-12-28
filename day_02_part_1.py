data = open('day_02_input.txt').read().splitlines()

score = 0
for game in data:
    opponent_turn, result = game.split()

    if result == 'X':
        if opponent_turn == 'A':
            card = 'C'
        elif opponent_turn == 'B':
            card = 'A'
        elif opponent_turn == 'C':
            card = 'B'

    elif result == 'Y':
        card = opponent_turn
        score += 3

    elif result == 'Z':
        score += 6
        if opponent_turn == 'A':
            card = 'B'
        elif opponent_turn == 'B':
            card = 'C'
        elif opponent_turn == 'C':
            card = 'A'
 
    if card == 'A':
        score += 1
    elif card == 'B':
        score += 2
    elif card == 'C':
        score += 3
    
print(score)