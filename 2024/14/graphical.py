import math
from PIL import Image, ImageDraw

with open("input.txt") as file:
    LINES = file.read().strip().splitlines()

robots = []
for line in LINES:
    line = line.replace('p=', '')
    line = line.replace('v=', '')
    robots.append([int(y) for z in [x.split(',') for x in line.split()] for y in z])

ROOM_WIDTH, ROOM_HEIGHT = 101, 103

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

    img = Image.new('RGB', (ROOM_WIDTH, ROOM_HEIGHT), color='white')
    draw = ImageDraw.Draw(img)

    for row in range(ROOM_HEIGHT):
        for col in range(ROOM_WIDTH):
            if (col, row) in final_positions:
                draw.point((col, row), fill='red')
            else:
                draw.point((col, row), fill='black')

    img.save(f'image_{SIMULATE_FOR}.png')
