import heapq
import math
from copy import deepcopy

with open('input.txt') as file:
    lines = [line.split('\n') for line in file.read().split('\n\n')]

monkeys = []
for line in lines:
    temp_dict = {}
    monkey = int(line[0].split(' ')[1][:-1])
    temp_dict['items'] = list(map(int, line[1].split('Starting items: ')[1:].pop().split(', ')))
    temp_dict['operation'] = line[2].split('Operation: new = ')[1:].pop()
    temp_dict['test'] = int(line[3].split('Test: divisible by ')[1:].pop())
    temp_dict['if_true'] = int(line[4].split('If true: throw to monkey ')[1:].pop())
    temp_dict['if_false'] = int(line[5].split('If false: throw to monkey ')[1:].pop())
    temp_dict['inspections'] = 0
    monkeys.append(temp_dict)
div_by = math.lcm(*[i['test'] for i in monkeys])


def main(it):
    monkeys_temp = deepcopy(monkeys)
    for i in range(it):
        for line in monkeys_temp:
            for item in line['items']:
                old = item
                worry = eval(line['operation'])
                if it == 20:
                    worry = worry // 3
                elif it == 10_000:
                    worry = worry % div_by
                if worry % line['test'] == 0:
                    monkeys_temp[line['if_true']]['items'].append(worry)
                else:
                    monkeys_temp[line['if_false']]['items'].append(worry)
                line['inspections'] += 1
            line['items'] = []
    return (i['inspections'] for i in monkeys_temp)


print(math.prod(heapq.nlargest(2, main(20))))
print(math.prod(heapq.nlargest(2, main(10_000))))
