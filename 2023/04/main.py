import re

with open('input.txt') as file:
    lines = file.read().strip().splitlines()

part1 = 0
part2_cards = [1 for _ in range(len(lines))]
for line in lines:
    x = line.split('|')
    game, *winning_cards = list(map(int, re.findall(r'\d+', x[0])))
    my_cards = list(map(int, re.findall(r'\d+', x[1])))

    matches = 0
    for match in my_cards:
        if match in winning_cards:
            matches += 1
    part1 += int(2 ** (matches - 1))
    for i in range(game, game + matches):
        part2_cards[i] += part2_cards[game - 1]

print(part1)
print(sum(part2_cards))
