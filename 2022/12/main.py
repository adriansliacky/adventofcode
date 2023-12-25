from collections import deque

with open('input.txt') as file:
    lines = file.read().rstrip().splitlines()
    pos_s = next((i, j.index('S')) for i, j in enumerate(lines) if 'S' in j)
    pos_e = next((i, j.index('E')) for i, j in enumerate(lines) if 'E' in j)
    lines = [line.replace('E', 'z') for line in [line.replace('S', 'a') for line in lines]]

valid = lambda pos_x, pos_y: 0 <= pos_x < len(lines) and 0 <= pos_y < len(lines[0])
moves, steps = {}, {}
for pos_s_x, pos_s_y in [(i, j) for i in range(len(lines)) for j in range(len(lines[0]))]:
    if lines[pos_s_x][pos_s_y] == 'a':
        queue = deque([(pos_s_x, pos_s_y)])
        steps[(pos_s_x, pos_s_y)] = 0
        while queue:
            x, y = queue.popleft()
            for x2, y2 in [(x + nx, y + ny) for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]]:
                if valid(x2, y2) and (((x2, y2) not in steps) or (steps[(x2, y2)] > steps[(x, y)] + 1)):
                    if ord(lines[x2][y2]) <= ord(lines[x][y]) + 1:
                        steps[(x2, y2)] = steps[(x, y)] + 1
                        queue.append((x2, y2))
        moves[(pos_s_x, pos_s_y)] = steps.get(pos_e, 1e6)
print(moves[pos_s])
print(min(moves.values()))
