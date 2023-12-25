with open('input.txt') as file:
    LINES = file.read().strip().splitlines()

DIRS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
hexDIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
total = 0

x, y = 0, 0
left_lines = []
right_lines = []
bottom = 0
last_dir = DIRS[LINES[-1].split()[0]]
for i, line in enumerate(LINES):
    directions, steps, hex = line.split()
    hex_steps = int(steps) + 1
    dx, dy = DIRS[directions]

    try:
        next_dir = DIRS[LINES[i + 1].split()[0]]

    except IndexError:
        pass

    if (dx, dy) == (0, 1) and next_dir == (-1, 0):
        hex_steps -= 1
    elif (dx, dy) == (0, -1) and next_dir == (1, 0):
        hex_steps -= 1
    if (dx, dy) == (0, 1) and last_dir == (1, 0):
        hex_steps -= 1
    elif (dx, dy) == (0, -1) and last_dir == (-1, 0):
        hex_steps -= 1

    nx, ny = x + dx * (hex_steps - 1), y + dy * hex_steps

    line_data = (x, hex_steps)

    if (dx, dy) == (0, -1):
        left_lines.append(line_data)
    elif (dx, dy) == (0, 1):
        right_lines.append(line_data)
    else:
        bottom = max(bottom, nx + 1)
    last_dir = (dx, dy)
    x, y = nx, ny

for x, steps in right_lines:
    total += (bottom - x) * steps
for x, steps in left_lines:
    total -= (bottom - x - 1) * steps

print(total)

x, y = 0, 0
left_lines = []
right_lines = []
bottom = 0
total = 0
last_dir = hexDIRS[int(LINES[-1].split()[2][-2])]
for i, line in enumerate(LINES):
    directions, steps, hex = line.split()
    hex_steps = int(hex[2:-2], 16) + 1
    # hex_steps = int(steps) + 1
    dx, dy = hexDIRS[int(hex[-2])]
    # dx, dy = DIRS[directions]

    try:
        next_dir = hexDIRS[int(LINES[i + 1].split()[2][-2])]
        # next_dir = DIRS[LINES[i + 1].split()[0]]

    except IndexError:
        pass

    if (dx, dy) == (0, 1) and next_dir == (-1, 0):
        hex_steps -= 1
    elif (dx, dy) == (0, -1) and next_dir == (1, 0):
        hex_steps -= 1
    if (dx, dy) == (0, 1) and last_dir == (1, 0):
        hex_steps -= 1
    elif (dx, dy) == (0, -1) and last_dir == (-1, 0):
        hex_steps -= 1

    nx, ny = x + dx * (hex_steps - 1), y + dy * hex_steps

    line_data = (x, hex_steps)

    if (dx, dy) == (0, -1):
        left_lines.append(line_data)
    elif (dx, dy) == (0, 1):
        right_lines.append(line_data)
    else:
        bottom = max(bottom, nx + 1)
    last_dir = (dx, dy)
    x, y = nx, ny

for x, steps in right_lines:
    total += (bottom - x) * steps
for x, steps in left_lines:
    total -= (bottom - x - 1) * steps

print(total)
