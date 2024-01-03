data = [[direction.split()[0], int(direction.split()[1])] for direction in open('day_09_input.txt')]

current_place_head = [0,0]
current_place_tail = [0,0]
destinations = set()
destinations.add((0,0))

for direction, steps in data:
    for count in range(steps):

        if direction == 'R':
            current_place_head[1] += 1         
        elif direction == 'L':
            current_place_head[1] -= 1
        elif direction == 'U':
            current_place_head[0] -= 1
        elif direction == 'D':
            current_place_head[0] += 1                

        difference_rows = current_place_head[0] - current_place_tail[0]
        difference_columns = current_place_head[1] - current_place_tail[1]

        if abs(difference_rows) > 1 or abs(difference_columns) > 1:
            if difference_rows == 0:
                current_place_tail[1] += difference_columns // 2 
            elif difference_columns == 0:
                current_place_tail[0] += difference_rows // 2
            else:
                current_place_tail[0] += 1 if difference_rows > 0 else - 1
                current_place_tail[1] += 1 if difference_columns > 0 else - 1

        destinations.add((current_place_tail[0], current_place_tail[1]))

number_of_unique_destinations = len(destinations)
print(number_of_unique_destinations)