import collections

with open('input.txt') as file:
    LINES = file.read().strip().splitlines()

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # R, D, L, U


def bfs(_x, _y, _d):
    energized = set()
    queue = collections.deque()
    queue.append((_x, _y, _d))
    seen = set()
    i = 0
    while queue:
        x, y, direction = queue.popleft()
        seen_dir = direction

        if (x, y, direction) not in seen and 0 <= x < len(LINES) and 0 <= y < len(LINES[0]):
            energized.add((x, y))
            char = LINES[x][y]
            if char == '\\':
                if direction == 0:  # right
                    direction = 1
                elif direction == 1:  # down
                    direction = 0
                elif direction == 2:  # left
                    direction = 3
                elif direction == 3:  # up
                    direction = 2
                queue.append((x + DIRS[direction][0], y + DIRS[direction][1], direction))
            elif char == '/':
                if direction == 0:  # right
                    direction = 3
                elif direction == 1:  # down
                    direction = 2
                elif direction == 2:  # left
                    direction = 1
                elif direction == 3:  # up
                    direction = 0
                queue.append((x + DIRS[direction][0], y + DIRS[direction][1], direction))
            elif char == '-' and direction in (1, 3):
                queue.append((x, y + 1, 0))
                queue.append((x, y - 1, 2))
            elif char == '|' and direction in (0, 2):
                queue.append((x + 1, y, 1))
                queue.append((x - 1, y, 3))
            else:
                queue.append((x + DIRS[direction][0], y + DIRS[direction][1], direction))
            seen.add((x, y, seen_dir))
    return len(energized)


part2 = 0
for y in range(len(LINES[0])):
    part2 = max(part2, bfs(0, y, 1), bfs(len(LINES), y, 3))
part1 = bfs(0, 0, 0)
for x in range(len(LINES)):
    part2 = max(part2, bfs(x, 0, 0), bfs(x, len(LINES[0]), 2))
print(part1)
print(part2)
