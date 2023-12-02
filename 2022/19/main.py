import re
from collections import deque
from math import prod

with open('input.txt') as file:
    lines = file.read().rstrip().splitlines()

robots_blueprints = []
for line in lines:
    bp_id, ore_ore, clay_ore, obs_ore, obs_clay, geo_ore, geo_obs = map(int, re.findall(r'\d+', line))
    robots_blueprints.append({
        'geo': {'ore': geo_ore, 'obs': geo_obs},
        'obs': {'ore': obs_ore, 'clay': obs_clay},
        'clay': {'ore': clay_ore},
        'ore': {'ore': ore_ore}
    })


def solve(minutes):
    geo_ar = []
    for _bp_id, robots in enumerate(robots_blueprints):
        resources = {i: 0 for i in robots}
        robots_bool = {i: (i == 'ore') for i in robots}
        queue = deque([(minutes, resources, robots_bool, -1)])
        max_geo = 0

        while queue:
            (time_minutes, resources, robots_bool, last) = queue.pop()
            if time_minutes == 0:
                max_geo = max(max_geo, resources['geo'])
                continue
            if (time_minutes * (2 * robots_bool['geo'] + time_minutes)) // 2 <= max_geo - resources['geo']:
                continue
            wait_for_rob = False
            for robot_t, res in robots.items():
                if all(j <= resources[i] - robots_bool[i] for i, j in res.items()) and (last == robot_t or last == -1):
                    continue
                if any(resources[i] < j for i, j in res.items()):
                    wait_for_rob = all(0 < robots_bool[i] for i in res.keys()) or wait_for_rob
                    continue
                resources_use_next = {i: j + robots_bool[i] - res.get(i, 0) for i, j in resources.items()}
                robots_use_next = {i: j + (i == robot_t) for i, j in robots_bool.items()}
                queue.append(tuple([time_minutes - 1, resources_use_next, robots_use_next, robot_t]))
            if wait_for_rob:
                resources_use_next = {i: j + robots_bool[i] for i, j in resources.items()}
                queue.append(tuple([time_minutes - 1, resources_use_next, robots_bool, -1]))
        geo_ar.append(max_geo * (1 if minutes == 32 else _bp_id + 1))
        if (minutes == 32) and (_bp_id == 2):
            break
    return (sum(geo_ar)) if minutes == 24 else prod(geo_ar)


print(solve(24))
print(solve(32))
