import regex as re 

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "\d"]
data = open("./day1/data2.txt").readlines()
regex_obj = re.compile(r'(' + '|'.join(digits) + ')')

def digits_to_s(x):
    return str(digits.index(x) + 1) if digits.count(x) > 0 else x

def parse_line(x):
    digits = [digits_to_s(x) for x in regex_obj.findall(x, overlapped=True)]
    return int(digits[0] + digits[0] if digits.count == 1 else digits[0] + digits[-1])

answer = sum(parse_line(x) for x in data)

print(answer)