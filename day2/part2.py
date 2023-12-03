import regex as re
import math
data = open("./day2/data.txt").readlines()
regex_obj = re.compile(r'(\d{1,}|blue|red|green)')

def get_power(hands):
    min_cubes = { "blue": 0, "green": 0, "red": 0 }
    for count, color in zip(hands[::2], hands[1::2]):
        min_cubes[color] = max(int(count), min_cubes[color])
    return math.prod(min_cubes.values())

def get_points(game):
    parsed = regex_obj.findall(game)
    hands = parsed[1:]
    return get_power(hands)

ans = sum(get_points(x) for x in data)
print(ans)