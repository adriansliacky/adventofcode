import time

with open('input.txt') as file:
    lines = [[tuple(map(int, i.split(','))) for i in line.strip().split(" -> ")] for line in file.readlines()]

tiles = {}
for line in lines:
    for i in range(0, len(line) - 1):
        for x in range(min(line[i][0], line[i + 1][0]), max(line[i][0], line[i + 1][0]) + 1):
            for y in range(min(line[i][1], line[i + 1][1]), max(line[i][1], line[i + 1][1]) + 1):
                tiles[(x, y)] = 'r'
max_tiles = max([[k[1]] for k in tiles.keys()])[0]


def main(part1):
    global max_tiles
    if not part1:
        for x1 in range(0, 1001):
            for y1 in range(max_tiles + 2, max_tiles + 3):
                tiles[(x1, y1)] = 'r'
    max_tiles = max([[k[1]] for k in tiles.keys()])[0]
    p, i = 500, 0
    while max_tiles >= i:
        while True:
            if part1:
                if i > max_tiles:
                    break
            if (p, i + 1) not in tiles:
                i += 1
            elif (p - 1, i + 1) not in tiles:
                p -= 1
                i += 1
            elif (p + 1, i + 1) not in tiles:
                p += 1
                i += 1
            else:
                break
        tiles[(p, i)] = 's'
        if i <= max_tiles:
            p, i = 500, 0
        if not part1:
            if (500, 0) in tiles:
                break
    return sum([1 if v == 's' else 0 for v in tiles.values()]) - (1 if part1 else 0)


print(main(True))
print(main(False))
