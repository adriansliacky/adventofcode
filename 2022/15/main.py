"""
Use Pypy for best performance,
Pypy: around 4000ms (part1 and part2)
CPython: around 22secs(part1 and part2)
"""

import re

with open('input.txt') as file:
    coords = []
    for line in file.read().rstrip().splitlines():
        coords.append(([int(i) for i in re.findall(r'-?\d+', line)]))

total = set()
for (sen_x, sen_y, bec_x, bec_y) in coords:
    dist_s2b = abs((sen_x - bec_x)) + abs((sen_y - bec_y))
    dist_s2r = abs(sen_y - 2000000)

    if dist_s2b > dist_s2r:
        for i in range(abs(dist_s2b - dist_s2r) + 1):
            total.update([sen_x + i, sen_x - i])
    if bec_y == 2000000 and bec_x not in total:
        total.remove(bec_x)
print(len(total) - 1)


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged_ranges = []
    for i in range(len(ranges) - 1):
        r1 = ranges[i]
        r2 = ranges[i + 1]
        if r2[0] <= r1[1] <= r2[1] or r2[0] == r1[1] + 1:
            ranges[i + 1] = [r1[0], r2[1]]
        elif r1[0] <= r2[0] and r1[1] >= r2[1]:
            ranges[i + 1] = r1
            continue
        else:
            merged_ranges.append(r1)
    merged_ranges.append(ranges[-1])
    return merged_ranges


for r in range(4000001):
    bcns = []
    for (sen_x, sen_y, bec_x, bec_y) in coords:
        dist_s2b = abs((sen_x - bec_x)) + abs((sen_y - bec_y))
        r_dist_d2b = dist_s2b - abs(r - sen_y)
        if r_dist_d2b < 0:
            continue
        bcns.append(
            [sen_x - r_dist_d2b, sen_x + r_dist_d2b]
        )
    rangs = merge_ranges(bcns)
    if len(rangs) > 1:
        print(4000000 * (rangs[0][1] + 1) + r)
        break
