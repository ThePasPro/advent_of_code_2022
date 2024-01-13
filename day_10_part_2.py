x = 1
o = []

data = open('day_10_input.txt')

for line in data:
    if line.split()[0] == "noop":
        o.append(x)
    else:
        v = int(line.split()[1])
        o.append(x)
        o.append(x)
        x += v

# for i in range(0, len(o), 40):
#     for j in range(40):
#         print(end = '#' if abs(o[i + j] - j) <= 1 else " ")
#     print()
        
print(o)

