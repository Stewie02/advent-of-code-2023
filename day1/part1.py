import re 

data = open("./day1/data.txt").readlines()
regex_obj = re.compile(r'\d')

def parse_line(x):
    digits = regex_obj.findall(x)

    return int(digits[0] + digits[0] if digits.count == 1 else digits[0] + digits[-1])

answer = sum(parse_line(x) for x in data)

print(answer)