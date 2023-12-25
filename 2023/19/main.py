import re
import collections
from copy import deepcopy
import math

with open('input.txt') as file:
    LINES = [line.split('\n') for line in file.read().split('\n\n')]

total = 0

workflows = {}
for workflow in LINES[0]:
    workflow_name, rules_string = workflow.split('{')
    rules = rules_string.rstrip('}').split(',')
    workflows[workflow_name.strip()] = rules

for part in LINES[1]:
    x, m, a, s = map(int, re.findall(r'\d+', part))
    resolve = {'x': x, 'm': m, 'a': a, 's': s}

    decided = False
    curr_workflow = 'in'
    while not decided:
        rules = workflows[curr_workflow]
        last = rules[-1]
        broke_out = False
        for rule in rules[:-1]:
            _if, _then = rule.split(':')
            parameter = _if[0]
            operator = _if[1]
            value = int(_if[2:])

            if operator == '<':
                if resolve[parameter] < value:
                    if _then == 'A':
                        total += sum(resolve.values())
                        decided = True
                        broke_out = True
                        break
                    elif _then == 'R':
                        decided = True
                        broke_out = True
                        break
                    else:
                        curr_workflow = _then.strip()
                        broke_out = True
                        break
            elif operator == '>':
                if resolve[parameter] > value:
                    if _then == 'A':
                        total += sum(resolve.values())
                        decided = True
                        broke_out = True
                        break
                    elif _then == 'R':
                        decided = True
                        broke_out = True
                        break
                    else:
                        curr_workflow = _then.strip()
                        broke_out = True
                        break

        if broke_out:
            continue

        if last == 'A':
            total += sum(resolve.values())
            decided = True
        elif last == 'R':
            decided = True
        else:
            curr_workflow = last.strip()
print(total)

total = 0

workflows = {}
for workflow in LINES[0]:
    workflow_name, rules_string = workflow.split('{')
    rules = rules_string.rstrip('}').split(',')
    parsed_rules = []
    for rule in rules[:-1]:
        _if, _then = rule.split(':')
        parameter = _if[0]
        operator = _if[1]
        value = int(_if[2:])
        parsed_rules.append((parameter, operator, value, _then.strip()))
    parsed_rules.append((rules[-1]))
    workflows[workflow_name.strip()] = parsed_rules

res = ['x', 'm', 'a', 's']
queue = collections.deque()
queue.append(('in', (1, 4000), (1, 4000), (1, 4000), (1, 4000)))
while queue:
    curr_workflow, *xmas = queue.popleft()
    rules = workflows[curr_workflow]
    last = rules[-1]
    broke_out = False
    for rule in rules[:-1]:
        parameter, operator, value, _then = rule
        if operator == '>':
            true_xmas = deepcopy(xmas)

            true_xmas[res.index(parameter)] = (
                max(value + 1, xmas[res.index(parameter)][0]), xmas[res.index(parameter)][1])

            xmas[res.index(parameter)] = (xmas[res.index(parameter)][0], min(value, xmas[res.index(parameter)][1]))

            if _then == 'A':
                total += math.prod([max(0, (b - a + 1)) for a, b in true_xmas])

            elif _then == 'R':
                continue
            else:
                queue.append((_then, *true_xmas))

        elif operator == '<':
            true_xmas = deepcopy(xmas)

            true_xmas[res.index(parameter)] = (
                xmas[res.index(parameter)][0], min(value - 1, xmas[res.index(parameter)][1]))

            xmas[res.index(parameter)] = (max(value, xmas[res.index(parameter)][0]), xmas[res.index(parameter)][1])

            if _then == 'A':
                total += math.prod([max(0, (b - a + 1)) for a, b in true_xmas])

            elif _then == 'R':
                continue
            else:
                queue.append((_then, *true_xmas))

    if last == 'A':
        total += math.prod([max(0, (b - a + 1)) for a, b in xmas])
        continue
    elif last == 'R':
        continue
    queue.append((last, *xmas))

print(total)
