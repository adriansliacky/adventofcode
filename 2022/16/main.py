"""
Use PyPy for best performance
"""

import re

with open('input.txt') as file:
    lines = file.read().splitlines()

start_vault, start_time, start_time_el = 'AA', 30, 26
valves, combinations, el, flow_filtered = {}, {}, {}, []
for line in lines:
    flow_rate = int(re.findall(r'-?\d+', line).pop())
    val_ids = re.findall(r'\b[A-Z]{2,}\b', line)
    x = [flow_rate]
    for j in range(len(val_ids)):
        x.insert(j + 1, val_ids[j])
    valves[val_ids[0]] = x
    if flow_rate > 0:
        flow_filtered.append(x[1])
vals = valves.values()
for pair1 in vals:
    for pair2 in vals:
        if pair1 == pair2:
            combinations[(pair1[1], pair2[1])] = 0
        else:
            combinations[(pair1[1], pair2[1])] = 1e9
for _ in range(len(valves)):
    for pair1 in vals:
        for pair2 in vals:
            for m in pair2[2:]:
                combinations[(pair1[1], m)] = min(combinations[(pair1[1], m)], combinations[(pair1[1], pair2[1])] + 1)


def solve(elephant, time_remaining, moves, score, curr_valve):
    if time_remaining <= 1:
        if elephant:
            el_moves = frozenset(moves)
            if el_moves in el:
                return el[el_moves] + score
            else:
                el[el_moves] = solve(not elephant, start_time_el, moves, 0, start_vault)
            return el[el_moves] + score
        else:
            return score
    if valves[curr_valve][0] > 0:
        time_remaining -= 1
        score += time_remaining * valves[curr_valve][0]
    result = score
    for valve in flow_filtered:
        if valve in moves:
            continue
        moves.add(valve)
        result = max(solve(elephant, time_remaining - (combinations[curr_valve, valve]), moves, score, valve), result)
        moves.remove(valve)
    return result


print(solve(False, start_time, set(), 0, start_vault))
print(solve(True, start_time_el, set(), 0, start_vault))
