data = open('day_03_input.txt').read().splitlines()

total = 0
for rucksack in data:
    common_items = []

    total_items = int(len(rucksack))
    half = int(total_items / 2)
    first_rucksack = rucksack[:half]
    second_rucksack = rucksack[half:]

    for character in first_rucksack:
        if character in second_rucksack:
            if character not in common_items:
                common_items.append(character)

                if character.islower():
                    priority = ord(character) - ord('a') + 1
                    total += priority
                else:
                    priority = ord(character) - ord('A') + 27
                    total += priority

print(total)