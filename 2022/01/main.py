with open('input.txt') as file:
    lines = file.read().strip().split('\n\n')

cal = sorted([sum(map(int, line.split('\n'))) for line in lines])

print(cal[-1])
print(sum(cal[-3:]))
