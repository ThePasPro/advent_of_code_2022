data = open('day_01_input.txt').read().splitlines()

list = [0]
for line in data:
    if line == '':
        list.append(0)
    else:
        list[-1] += int(line)

list.sort(reverse=True)
list = list[0:3]
print(sum(list))
