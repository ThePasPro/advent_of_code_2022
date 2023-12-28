data = open('day_01_input.txt').read().splitlines()

list = [0]

for line in data:
    if line == '':
        list.append(0)
    else:
        list[-1] += int(line)

print(max(list))



