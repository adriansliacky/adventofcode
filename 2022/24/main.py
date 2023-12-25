from collections import deque

with open('input.txt') as file:
    lines = file.read().rstrip().splitlines()

start_pos = (lines[0].index('.') - 1, 1)
end_pos = (len(lines) - 1, lines[-1].index('.'))

blizzards, wall = set(), set()
blizz_cycle = (len(lines) - 2) * (len(lines[0]) - 2)

dirs = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 0)]

for y_pos, row in enumerate(lines):
    for x_pos, c in enumerate(row):
        if c == '#':
            wall.add((y_pos, x_pos))
        elif c in dirs.keys():
            blizzards.add(((y_pos, x_pos), c))


def move_blizz(blizz):
    b_positions = []
    for (bx, by), di_c in blizz:
        x, y = (bx + dirs[di_c][0]), (by + dirs[di_c][1])
        if x == 0:
            x = len(lines) - 2
        elif x == len(lines) - 1:
            x = 1
        if y == 0:
            y = len(lines[0]) - 2
        elif y == len(lines[0]) - 1:
            y = 1
        b_positions.append(((x, y), di_c))
    return b_positions


blizzard_map = []
for i in range(blizz_cycle):
    bad = {b_pos for b_pos, di_c in blizzards}
    blizzard_map.append(bad)
    blizzards = move_blizz(blizzards)


def solve(start, end):
    queue = deque([start])
    seen = {start}
    while queue:
        (pos_x, pos_y), minutes = queue.popleft()
        nxt_minutes = (minutes + 1) % blizz_cycle
        nxt_blizz = blizzard_map[((minutes % blizz_cycle + 1) % blizz_cycle)]
        for (nx, ny) in possible_moves:
            x, y = pos_x + nx, pos_y + ny
            if (x, y) == end:
                return minutes
            if (x, y) not in nxt_blizz and 0 <= x < len(lines) and 0 <= y < len(lines[0]) and (
                    x, y) not in wall and (
                    (x, y), nxt_minutes) not in seen:
                seen.add(((x, y), nxt_minutes))
                queue.append(((x, y), nxt_minutes))


part1_minutes = solve((start_pos, 0), end_pos) + 1
print(part1_minutes)  # part 1
print(solve((start_pos, solve((end_pos, part1_minutes), start_pos) + 1), end_pos) + 1)  # part 2
