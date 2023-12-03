# I know the code is a mess. After debugging for so long I don't really care anymore...

data = open("./day3/data.txt").read().splitlines()
matrix = [[None for _ in range(len(line))] for line in data]

def check_neighbours(line_index, char_index):
    for line in range(line_index - 1, line_index + 2):
        for char in range(char_index - 1, char_index + 2):
            if line == -1 or char == -1 or line >= len(data) or char >= len(data[0]):
                continue
            cur = data[line][char]
            if not cur.isdigit() and cur != '.': return True

def fill_matrix(line, line_index):
    current_number = { "num": "", "valid": False }
    for char_index, x in enumerate(line):
        if x.isdigit():
            current_number["num"] += x
            if check_neighbours(line_index, char_index): current_number["valid"] = True
        else:
            if len(current_number["num"]) > 0 and current_number["valid"]:
                for i in range(len(current_number["num"])):
                    matrix[line_index][char_index - i - 1] = int(current_number["num"])
            current_number = { "num": "", "valid": False }
    if current_number["valid"]:
        for i in range(len(current_number["num"])):
            matrix[line_index][len(matrix[line_index]) - i - 1] = int(current_number["num"])

def get_gear_neighbours(line_index, char_index):
    neighbours = []
    for line in range(line_index - 1, line_index + 2):
        can_add = True
        for char in range(char_index - 1, char_index + 2):
            if line == -1 or char == -1 or line >= len(data) or char >= len(data[0]):
                continue
            num = matrix[line][char]
            if isinstance(num, int) and can_add:
                neighbours.append(num)
                can_add = False
            elif not isinstance(num, int):
                can_add = True
    return neighbours

def get_total():
    total = 0
    count = 0
    for line_index, line in enumerate(data):
        for char_index, char in enumerate(line):
            if char == "*":
                count += 1
                nums = get_gear_neighbours(line_index, char_index)
                if count == 2:
                    print("The nums are: ", ", ".join(str(x) for x in nums))
                if len(nums) == 2:
                    print(nums[0], "", nums[1], end="\n\n\n")
                    total += nums[0] * nums[1]
    return total

for i, x in enumerate(data): fill_matrix(x, i)

print(get_total())

