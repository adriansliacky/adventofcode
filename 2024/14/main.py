import math
from collections import Counter

with open("input.txt") as file:
    LINES = file.read().strip().splitlines()

robots = []
for line in LINES:
    line = line.replace('p=', '')
    line = line.replace('v=', '')
    robots.append([int(y) for z in [x.split(',') for x in line.split()] for y in z])

ROOM_WIDTH, ROOM_HEIGHT = 101, 103


def calculate_entropy(positions):
    position_counts = Counter(positions)
    total_positions = len(positions)
    probabilities = [count / total_positions for count in position_counts.values()]
    return -math.log2(sum(p ** 2 for p in probabilities))


entropy = -1
result = 1
for SIMULATE_FOR in range(1, 10001):
    final_positions = set()
    if SIMULATE_FOR == 100:
        final_positions = []
    for px, py, vx, vy in robots:
        x = px + vx * SIMULATE_FOR
        y = py + vy * SIMULATE_FOR
        x = x % ROOM_WIDTH
        y = y % ROOM_HEIGHT
        if SIMULATE_FOR == 100:
            final_positions.append((x, y))
        else:
            final_positions.add((x, y))

    if SIMULATE_FOR == 100:
        HALF_WIDTH = (ROOM_WIDTH - 1) // 2
        HALF_HEIGHT = (ROOM_HEIGHT - 1) // 2
        quadrants = [0, 0, 0, 0]
        for (x, y) in final_positions:
            if 0 <= x < HALF_WIDTH and 0 <= y < HALF_HEIGHT:
                quadrants[0] += 1
            elif HALF_WIDTH < x and 0 <= y < HALF_HEIGHT:
                quadrants[1] += 1
            elif HALF_WIDTH < x and HALF_HEIGHT < y:
                quadrants[2] += 1
            elif 0 <= x < HALF_WIDTH and HALF_HEIGHT < y:
                quadrants[3] += 1
        print(math.prod(quadrants))

    curr_entropy = calculate_entropy(final_positions)
    if curr_entropy > entropy:
        entropy = curr_entropy
        result = SIMULATE_FOR
print(result)
