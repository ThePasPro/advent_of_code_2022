data = open('day_06_input.txt').read()

marker = []
for index, character in enumerate(data):
    marker.append(character)
    if len(marker) == 15:
        marker.remove(marker[0])

    unique = set(marker)
    if len(unique) == 14:
        print(index + 1)
        break