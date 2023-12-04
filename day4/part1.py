import regex as re

regex = re.compile(r'\d{1,}|\|')
data = open("./day4/data.txt").read().splitlines()

def get_line_points(line):
    parsed = regex.findall(line)
    seperator = parsed.index("|")
    winning = parsed[1:seperator]
    numbers = parsed[seperator + 1:]

    amount = 0
    for x in numbers:
        if winning.count(x) > 0: 
            amount += 1
    if amount == 0: return 0
    return 1 if amount == 1 else 2 ** (amount - 1)

print(sum(get_line_points(x) for x in data))
