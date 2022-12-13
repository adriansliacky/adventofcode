with open('input.txt') as file:
    lines = file.read().splitlines()

x, i, j, total, exe = 1, 0, 0, 0, lambda: (x * i) if i in [20, 60, 100, 140, 180, 220] else 0


def func():
    if i % 40 == 0:
        print()
    if i % 40 in range(x - 1, x + 2):
        print('█', end='▓')
    else:
        print(' ', end=' ')


for line in lines:
    cmd = line.split()
    if len(cmd) == 2:
        func()
        i += 1
        total += exe()
        func()
        i += 1
        total += exe()
        x += int(cmd[1])
    elif len(cmd) == 1:
        func()
        i += 1
        total += exe()

print(f'\n\n{total}')
