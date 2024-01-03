import re

data = open('day_05_input.txt')

crates = []
for line in data:
    if line == "\n": break
    crates.append([line[character * 4 + 1] for character in range(len(line) // 4)])

crates.pop()
crates = [list(''.join(crate).strip())[::-1] for crate in zip(*crates)]

for line in data:
    amount_of_crates, start_number, end_number = map(int, re.findall("\\d+", line))

    
    crates[end_number - 1].extend(crates[start_number - 1][-amount_of_crates:])
    crates[start_number - 1] = crates[start_number - 1][:-amount_of_crates]


print("".join([amount_of_crates[-1] for amount_of_crates in crates]))

