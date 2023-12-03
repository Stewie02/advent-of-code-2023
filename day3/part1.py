# I know the code is a mess. After debugging parrt2 for so long I don't really care anymore...

data = open("./day3/data.txt").read().splitlines()

def check_neighbours(line_index, char_index):
    for line in range(line_index - 1, line_index + 2):
        for char in range(char_index - 1, char_index + 2):
            if line == -1 or char == -1 or line >= len(data) or char >= len(data[0]):
                continue
            cur = data[line][char]
            if not cur.isdigit() and cur != '.': return True

def get_line_value(line, line_index):
    total = 0
    current_number = { "num": "", "valid": False }
    for char_index, x in enumerate(line):
        if x.isdigit():
            current_number["num"] += x
            if check_neighbours(line_index, char_index): current_number["valid"] = True
        else:
            if len(current_number["num"]) > 0 and current_number["valid"]:
                total += int(current_number["num"])
            current_number = { "num": "", "valid": False }
    if current_number["valid"]: total += int(current_number["num"])
    return total

total = sum(get_line_value(x, i) for i, x in enumerate(data))

print(total)

