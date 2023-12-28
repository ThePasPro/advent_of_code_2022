data = open('day_04_input.txt').read().splitlines()

total = 0
for pair in data:
    sections_elf_1 = []
    sections_elf_2 = []

    elf_1, elf_2 = pair.split(',')

    start_1, stop_1 = elf_1.split('-')
    start_2, stop_2 = elf_2.split('-')

    total_sectons_elf_1 = int(stop_1) - int(start_1) + 1
    total_sectons_elf_2 = int(stop_2) - int(start_2) + 1

    for section in range(int(start_1), int(stop_1) + 1):
        sections_elf_1.append(section)
    
    for section in range(int(start_2), int(stop_2) + 1):
        sections_elf_2.append(section)

    print(sections_elf_1, sections_elf_2)

    equal_sections_elf_1 = 0
    for section in sections_elf_1:
        if section in sections_elf_2:
            equal_sections_elf_1 += 1

    equal_sections_elf_2 = 0
    for section in sections_elf_2:
        if section in sections_elf_1:
            equal_sections_elf_2 += 1

    if equal_sections_elf_1 == total_sectons_elf_1:
        total += 1
    elif equal_sections_elf_2 == total_sectons_elf_2:
        total += 1


print(total)   