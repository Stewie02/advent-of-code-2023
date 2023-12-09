import regex as re
import math

data = open("./data.txt").read().splitlines()
network = {}
instructions = data[0]
regex = re.compile(r'[A-Z]{3}')

for line in data[2:]:
    matches = regex.findall(line)
    network[matches[0]] = (matches[1], matches[2])

def get_step_count(current):
    steps, found = 0, False
    instr_index = 0

    while not found:
        steps += 1
        instr = instructions[instr_index]

        current = network[current][0 if instr == "L" else 1]

        if current[-1] == "Z": found = True
        instr_index += 1
        instr_index %= len(instructions)
    return steps

counts = [get_step_count(x) for x in network.keys() if x[-1] == "A"]

print(math.lcm(*counts))

