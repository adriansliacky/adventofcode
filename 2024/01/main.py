from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read().strip().splitlines()
    first, second = [], []
    for x in data:
        x = [int(y) for y in x.split('   ')]
        first.append(x[0])
        second.append(x[1])


first.sort()
second.sort()

total = 0
for each in zip(first, second):
    total += abs(each[0] - each[1])

print(total)
counter = Counter(second)
total = 0
for x in first:
    total += x * counter[x]

print(total)