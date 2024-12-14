from collections import deque

with open("input.txt") as file:
    LINES = [[int(y) for y in x if y] for x in file.read().strip().splitlines()]


def bfs_p1(y, x):
    visited = set()
    queue = deque()
    queue.append((y, x))
    score = 0
    while queue:
        y, x = queue.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        current = LINES[y][x]
        if current == 9:
            score += 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_y, n_x = y + dy, x + dx
            if 0 <= n_y < len(LINES) and 0 <= n_x < len(LINES[0]) and LINES[n_y][n_x] == current + 1:
                queue.append((n_y, n_x))
    return score


def bfs_p2(y, x):
    queue = deque()
    queue.append((y, x))
    score = 0
    while queue:
        y, x = queue.popleft()
        current = LINES[y][x]
        if current == 9:
            score += 1
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            n_y, n_x = y + dy, x + dx
            if 0 <= n_y < len(LINES) and 0 <= n_x < len(LINES[0]) and LINES[n_y][n_x] == current + 1:
                queue.append((n_y, n_x))
    return score


total = 0
total_2 = 0
for row in range(len(LINES)):
    for col in range(len(LINES[0])):
        if LINES[row][col] == 0:
            total += bfs_p1(row, col)
            total_2 += bfs_p2(row, col)

print(total)
print(total_2)
