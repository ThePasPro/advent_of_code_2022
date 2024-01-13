data = open('day_11_input.txt').read().strip().split('\n\n')

monkeys = []
for monkey in data:
    lines = monkey.splitlines()   
    items = [int(num.strip()) for num in lines[1].split(':')[1].strip().split(',')]
    operation = lines[2].split()[-1]
    test = int(lines[3].split()[-1])
    monkey_true = int(lines[4].split()[-1])
    monkey_false = int(lines[5].split()[-1])
    
    if '+' in lines[2].split():
        operation_symbol = '+'
    elif '*' in lines[2].split():
        operation_symbol = '*'

    monkeys.append([items, operation, operation_symbol, test, monkey_true, monkey_false])


worry_level = 0
counts = [0] * len(monkeys)
for _ in range(20):
    for index, monkey in enumerate(monkeys):
        item_list = monkey[0]
        operation = monkey[1]
        operation_symbol = monkey[2]
        test = monkey[3]
        monkey_when_true = monkey[4]
        monkey_when_false = monkey[5]
        counts[index] += len(item_list)

        for item in item_list:
            if operation == 'old':
                if '+' in operation_symbol:
                    worry_level = item + item
                    symbol = '+'
                else:
                    worry_level = item * item
                    symbol = '*'
            else:
                if '+' in operation_symbol:
                    worry_level = item + int(operation)
                    symbol = '+'
                else:
                    worry_level = item * int(operation)
                    symbol = '*'

            worry_level //=3          
            if worry_level % monkey[3] == 0:
                new_monkey = monkey[4]
                monkeys[new_monkey][0].append(worry_level)
            else:
                new_monkey = monkey[5]
                monkeys[new_monkey][0].append(worry_level)
        
        monkey[0] = []

counts.sort(reverse=True)
print(counts[0] * counts[1])