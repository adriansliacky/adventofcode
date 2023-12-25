import collections

with open('input.txt') as file:
    LINES = file.read().strip().splitlines()

DIRS = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
hexDIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
total = 0

# x, y = 0, 0
# coords = set()
# for line in LINES:
#     directions, steps, hex = line.split()
#     hex_steps = int(hex[2:-2], 16)
#     steps = int(steps)
#     for _ in range(hex_steps):
#         dx, dy = hexDIRS[int(hex[-2])]
#         x += dx
#         y += dy
#         coords.add((x, y))

x, y = 0, 0
coords = set()
for line in LINES:
    directions, steps, *_ = line.split()
    steps = int(steps)
    for _ in range(steps):
        dx, dy = DIRS[directions]
        x += dx
        y += dy
        coords.add((x, y))


# sorted_coords = sorted(coords, key=lambda x: (x[0], x[1]))
# grouped = {}
# for a, b in sorted_coords:
#     if a in grouped:
#         grouped[a].append(b)
#     else:
#         grouped[a] = [b]
#
# result = list(grouped.values())


def floodfill(x, y):
    checked = set()
    visited = set()

    def check_validity(_x, _y):
        if (_x, _y) in checked:
            return False
        checked.add((_x, _y))
        return (grid[_x][_y] != '#') and ((_x, _y) not in visited)

    q = collections.deque()
    q.append((x, y))
    while q:
        (x1, y1) = q.popleft()
        visited.add((x1, y1))

        # expand in all 4 directions
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            _x, _y = x1 + dx, y1 + dy
            if check_validity(_x, _y):
                q.append((_x, _y))
    return visited


grid = []
for x in range(min(x for x, y in coords), max(x for x, y in coords) + 1):
    sub_grid = []
    for y in range(min(y for x, y in coords), max(y for x, y in coords) + 1):
        if (x, y) in coords:
            sub_grid.append('#')
        else:
            sub_grid.append('.')
    grid.append(sub_grid)

start_coords = None
for x, row in enumerate(grid):
    b_out = False
    for y, char in enumerate(row):
        ny = y + 1 if 0 < y + 1 < len(row) - 1 else y
        if char == '#' and grid[x][ny] == '.':
            start_coords = (x, y)
            b_out = True
            break
    if b_out:
        break

start_coords = (1, 152)
# start_coords = (1, 1)

print(start_coords)
vis = floodfill(*start_coords)
# vis = set()
for x, row in enumerate(grid):
    for y, char in enumerate(row):
        if (x, y) in vis and False:
            print('O', end='')
        else:
            if char == '#':
                print('#', end='')
            elif char == '.':
                print(' ', end='')
    print()

total = len(coords) + len(vis)
print(total)
