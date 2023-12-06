# I am sorry for the ugly brute force method, but I couldn't care less after day 5 :P

import regex as re
import math

regex = re.compile(r'\d+')
data = open("./data.txt").read().splitlines()

def parse_line(line):
    numbers = regex.findall(line)
    return int("".join(numbers))


time, distance = [parse_line(x) for x in data]

has_won, wins, i = False, 0, 0
while True:
    race_time = time - i
    wins_game = race_time * i > distance
    if wins_game: 
        has_won = True
        wins += 1
    if has_won and not wins_game: break
    i += 1

print(wins)

