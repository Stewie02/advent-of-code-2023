import regex as re

regex = re.compile(r'\d{1,}|\|')
data = open("./day4/data.txt").read().splitlines()
extra_copies = [0 for _ in data]

def process_card(card):
    parsed = regex.findall(card)
    seperator = parsed.index("|")
    winning = parsed[1:seperator]
    numbers = parsed[seperator + 1:]
    card_index = int(parsed[0]) - 1

    amount = 0
    for x in numbers:
        if winning.count(x) > 0: 
            amount += 1
    for i in range(amount):
        if card_index + i + 1 >= len(data): continue
        extra_copies[card_index + i + 1] += (extra_copies[card_index] + 1)
    
for card in data: process_card(card)

print(len(data) + sum(extra_copies))
