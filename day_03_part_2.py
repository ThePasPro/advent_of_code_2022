data = open('day_03_input.txt').read().splitlines()

total = 0
grouped_elves = []

for i in range(0, len(data), 3):
    group = data[i:i+3] 
    grouped_elves.append(group)

for index, group in enumerate(grouped_elves):
    common_items = []
    for character in group[0]:
        if character in group[1] and character in group[2]:
            if character not in common_items:
                common_items.append(character)

                if character.islower():
                    priority = ord(character) - ord('a') + 1
                    total += priority
                else:
                    priority = ord(character) - ord('A') + 27
                    total += priority
    
print(total)