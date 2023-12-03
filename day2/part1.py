import regex as re

cubes_count = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

data = open("./day2/data.txt").readlines()
regex_obj = re.compile(r'(\d{1,}|blue|red|green)')

def check_hands(hands):
    for count, color in zip(hands[::2], hands[1::2]):
        if cubes_count[color] < int(count): return False
    return True

def get_points(game):
    parsed = regex_obj.findall(game)
    game_index, hands = int(parsed[0]), parsed[1:]
    possible = check_hands(hands)
    return game_index if possible else 0

ans = sum(get_points(x) for x in data)
print(ans)