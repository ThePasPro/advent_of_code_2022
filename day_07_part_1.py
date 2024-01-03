data = open('day_07_input.txt').read().splitlines()

directory = {'/':{}}

for line in data:
    if "/" in line:
        continue

    elif 'ls' in line:
        directory['/'][line] = 


print(directory)