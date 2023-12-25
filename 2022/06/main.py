with open('input.txt') as file:
    line = list(file.read())


def solve(n):
    for _, s in enumerate(line):
        if len(set(line[_: _ + n])) == n:
            print(_ + n)
            break


solve(4)
solve(14)
