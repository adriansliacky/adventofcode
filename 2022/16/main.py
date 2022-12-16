import re

with open('input.txt') as file:
    lines = file.read().splitlines()

start, time_rem = 'AA', 30
valves, combinations, flow_filtered, sols = {}, {}, [], []
for line in lines:
    flowrate = int(re.findall(r'-?\d+', line).pop())
    val_ids = re.findall(r'\b[A-Z]{2,}\b', line)
    x = [flowrate]
    for j in range(len(val_ids)):
        x.insert(j + 1, val_ids[j])
    valves[val_ids[0]] = x
    if flowrate > 0:
        flow_filtered.append(x[1])
vals = valves.values()
for pair1 in vals:
    for pair2 in vals:
        if pair1 == pair2:
            combinations[(pair1[1], pair2[1])] = 0
        else:
            combinations[(pair1[1], pair2[1])] = 100
for _ in range(len(valves)):
    for pair1 in vals:
        for pair2 in vals:
            for m in pair2[2:]:
                combinations[(pair1[1], m)] = min(combinations[(pair1[1], m)], combinations[(pair1[1], pair2[1])] + 1)


def solve_recursively(time_remaining, moves, score, curr_valve):
    if time_remaining < 1:
        return 0
    if valves[curr_valve][0] > 0:
        time_remaining -= 1
        score += time_remaining * valves[curr_valve][0]
    result = score
    for valve in flow_filtered:
        if valve in moves:
            continue
        moves.add(valve)
        sols.append(solve_recursively(time_remaining - (combinations[curr_valve, valve]), moves, score, valve))
        moves.remove(valve)
    return result


solve_recursively(time_rem, set(), 0, start)
print(max(sols))
