from functools import cmp_to_key

with open('input.txt', 'r') as file:
    data = file.read().strip().split('\n\n')
    order_rules = data[0].split('\n')
    order_rules = [[int(x) for x in rule.split('|')] for rule in order_rules]
    updates = data[1].split('\n')
    updates = [[int(x) for x in update.split(',')] for update in updates]

def compare(a, b):
    if [a, b] in order_rules:
        return -1
    elif [b, a] in order_rules:
        return 1
    return 0

total = 0
total2 = 0
for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(compare))
    if update == sorted_update:
        total += sorted_update[(len(sorted_update) - 1) // 2]
    else:
        total2 += sorted_update[(len(sorted_update) - 1) // 2]

print(total)
print(total2)