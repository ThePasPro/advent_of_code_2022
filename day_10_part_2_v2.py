program = open('day_10_input.txt')

cycle = 0
x = 1
sprite = [0, 1, 2]
crt = []
cycle_for_crt = 0

for line in program:
    instruction = line.split()[0]

    if instruction == 'noop':
        value = 0
        cycle += 1
        cycle_for_crt += 1 

        if cycle_for_crt - 1 in range(sprite[0], sprite[2] + 1):
            crt.append('#')
        else:
            crt.append('.')

        if cycle_for_crt == 39:
            cycle_for_crt = -1
        
    else:
        value = int(line.split()[1])

        values = []
        for step in range(2):
            cycle += 1
            x += value if step == 1 else 0
            values.append(x)  

            cycle_for_crt += 1 
            if cycle_for_crt - 1 in range(sprite[0], sprite[2] + 1):
                crt.append('#')
            else:
                crt.append('.')

            if cycle_for_crt == 39:
                cycle_for_crt = -1

    sprite[0] += value
    sprite[1] += value
    sprite[2] += value

print(''.join(crt[0:40]))
print(''.join(crt[40:80]))
print(''.join(crt[80:160]))
print(''.join(crt[160:200]))
print(''.join(crt[200:240]))