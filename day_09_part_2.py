data = [[direction.split()[0], int(direction.split()[1])] for direction in open('day_09_input.txt')]

destinations = set([(0,0)])
rope = [[0,0] for _ in range(10)]

for direction, steps in data:
    for count in range(steps):

        if direction == 'R':
            rope[0][1] += 1         
        elif direction == 'L':
            rope[0][1] -= 1
        elif direction == 'U':
            rope[0][0] -= 1
        elif direction == 'D':
            rope[0][0] += 1          

        for rope_piece in range(9):
            current_place_head = rope[rope_piece]
            current_place_tail = rope[rope_piece + 1]      

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

        destinations.add(tuple(rope[-1]))

number_of_unique_destinations = len(destinations)
print(number_of_unique_destinations)