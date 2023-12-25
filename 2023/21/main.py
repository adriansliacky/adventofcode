import collections

with open('test.txt') as file:
    LINES = file.read().strip().splitlines()

# start_coords = None
# for x, row in enumerate(LINES):
#     for y, char in enumerate(row):
#         if char == 'S':
#             start_coords = (x, y)
#
# queue = collections.deque()
# queue.append((start_coords, 1))
# HEIGHT = len(LINES)
# WIDTH = len(LINES[0])
# visited = set()
# seen = set()
# while queue:
#     coords, steps = queue.popleft()
#     x, y = coords
#     for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and LINES[nx][ny] != '#':
#             if steps == 64:
#                 visited.add((nx, ny))
#             else:
#                 add = ((nx, ny), steps + 1)
#                 if add not in seen:
#                     queue.append(add)
#                     seen.add(add)
#
# print(len(visited))

start_coords = None
for x, row in enumerate(LINES):
    for y, char in enumerate(row):
        if char == 'S':
            start_coords = (x, y)

queue = collections.deque()
queue.append((start_coords, 1))
HEIGHT = len(LINES)
WIDTH = len(LINES[0])
visited = set()
seen = set()
while queue:
    coords, steps = queue.popleft()
    x, y = coords
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and LINES[nx][ny] != '#':
            if steps == 64:
                visited.add((nx, ny))
            else:
                add = ((nx, ny), steps + 1)
                if add not in seen:
                    queue.append(add)
                    seen.add(add)

print(len(visited))
