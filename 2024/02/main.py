with open('input.txt') as file:
    data = [[int(y) for y in x.split()] for x in file.read().strip().splitlines()]


def is_safe(row):
    last = None
    increment = None
    for each in row:
        if last is None:
            last = each
            continue
        elif increment is None:
            inc = each - last
            increment = inc > 0
            if not 0 < abs(inc) < 4:
                return False
        else:
            inc = each - last
            if (inc > 0) != increment or not 0 < abs(inc) < 4:
                return False
        last = each
    return True


total = 0
save_with_removals = 0
for row in data:
    if is_safe(row):
        total += 1
    else:
        for i in range(len(row)):
            if is_safe([row[y] for y in range(len(row)) if y != i]):
                save_with_removals += 1
                break

print(total)
print(total + save_with_removals)
