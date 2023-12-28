data = open('day_04_input.txt')

total = 0
for pair in data:
    start_1, stop_1, start_2, stop_2 = map(int, pair.replace(',', '-').split('-'))
    print(set(range(start_1, stop_1 + 1)) & set(range(start_2, stop_2 + 1)))

print(total)
