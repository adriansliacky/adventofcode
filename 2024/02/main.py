with open('test.txt') as file:
    data = file.read().strip().splitlines()
    data = [[int(y) for y in x.split()] for x in data]

for row in data:
    increasing = None
    increment = None
    for each in row:
        if increasing is None and increment is None:
