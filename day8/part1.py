import regex as re

data = open("./data.txt").read().splitlines()
network = {}
instructions = data[0]
regex = re.compile(r'[A-Z]{3}')

for line in data[2:]:
    matches = regex.findall(line)
    network[matches[0]] = (matches[1], matches[2])

steps, found = 0, False
instr_index, current = 0, "AAA"

while not found:
    steps += 1
    instr = instructions[instr_index]

    current = network[current][0 if instr == "L" else 1]

    if current == "ZZZ": found = True
    instr_index += 1
    instr_index %= len(instructions)

print(steps)

