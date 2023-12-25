def solve(dirs):
    with open('input.txt') as file:
        LINES = file.read().strip().splitlines()

    start_coords = (0, LINES[0].index('.'))
    end_coords = (len(LINES) - 1, LINES[-1].index('.'))

    crossroads = [start_coords, end_coords]
    for x, row in enumerate(LINES):
        for y, char in enumerate(row):
            if char == '.':
                valid_neighbours = 0
                for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < len(LINES) and 0 <= ny < len(row) and LINES[nx][ny] != '#':
                        valid_neighbours += 1
                if valid_neighbours >= 3:
                    crossroads.append((x, y))

    graph = {coords: {} for coords in crossroads}
    for sx, sy in crossroads:
        queue = [(sx, sy, 0)]
        seen = set()
        seen.add((sx, sy))
        while queue:
            x, y, dist = queue.pop()
            for dx, dy in dirs[LINES[x][y]]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in seen and 0 <= nx < len(LINES) and 0 <= ny < len(LINES[0]) and LINES[nx][ny] != '#':
                    if (nx, ny) in crossroads and dist != 0:
                        graph[(sx, sy)][(nx, ny)] = dist + 1
                    else:
                        queue.append((nx, ny, dist + 1))
                        seen.add((nx, ny))

    seen = set()

    def dfs(pt):
        if pt == end_coords:
            return 0
        longest = -float('inf')
        seen.add(pt)
        for neighbour in graph[pt]:
            if neighbour not in seen:
                longest = max(longest, dfs(neighbour) + graph[pt][neighbour])
        seen.remove(pt)
        return longest

    total = dfs(start_coords)

    print(total)


solve({'^': [(-1, 0)], 'v': [(1, 0)], '<': [(0, -1)], '>': [(0, 1)], '.': [(-1, 0), (1, 0), (0, -1), (0, 1)], '#': []})
solve({'^': [(-1, 0), (1, 0), (0, -1), (0, 1)], 'v': [(-1, 0), (1, 0), (0, -1), (0, 1)],
       '<': [(-1, 0), (1, 0), (0, -1), (0, 1)], '>': [(-1, 0), (1, 0), (0, -1), (0, 1)],
       '.': [(-1, 0), (1, 0), (0, -1), (0, 1)], '#': []})
