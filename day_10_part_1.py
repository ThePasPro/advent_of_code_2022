program = open('day_10_input.txt')

cycle = 0
x = 1
total_signal_strength = 0
for line in program:
    instruction = line.split()[0]

    if instruction == 'noop':
        value = 0
        cycle += 1
        
        if cycle in range(20, 260, 40):
            signal_strength = cycle * x
            total_signal_strength += signal_strength
    else:
        value = int(line.split()[1])

        values = []
        for step in range(2):
            cycle += 1
            x += value if step == 1 else 0
            values.append(x)

            if cycle in range(20, 260, 40):
                signal_strength = cycle * values[0]
                total_signal_strength += signal_strength           

print(total_signal_strength)