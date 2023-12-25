from collections import deque

with open('input.txt') as file:
    lines = file.read().rstrip().splitlines()

cbs = {}
for line in lines:
    (x, y, z) = map(int, line.split(','))
    adj, cbs[(x, y, z)] = [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)], 6
    for nb in adj:
        if nb in cbs:
            cbs[(x, y, z)], cbs[nb] = cbs[(x, y, z)] - 1, cbs[nb] - 1
print(sum(cbs.values()))

cbs, visited = {cube: 0 for cube in cbs}, set()
mx = tuple(max(i) + 1 for i in zip(*cbs))
queue = deque([mn := tuple(min(i) - 1 for i in zip(*cbs))])

while queue:
    cur = queue.popleft()
    if cur in visited:
        continue
    visited.add(cur)
    for i in (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0):
        n = tuple(x + y for (x, y) in zip(cur, i))
        if all((o1 <= o2 <= o3) for (o1, o2, o3) in zip(mn, n, mx)):
            if n in cbs:
                cbs[n] += 1
            else:
                queue.append(n)
print(sum(cbs.values()))
