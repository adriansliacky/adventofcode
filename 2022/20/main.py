with open('input.txt') as file:
    f = file.read().rstrip().splitlines()
    temp1 = list(enumerate([(int(line)) for line in f]))
    temp2 = list(enumerate([(int(line) * 811589153) for line in f]))


def solve(part2):
    temp = temp2 if part2 else temp1
    get_line = lambda ln: ln % (len(temp))
    for _ in range(10 if part2 else 1):
        for i in range(len(temp)):
            n, pos = next((temp[j], j) for j in range(len(temp)) if temp[j][0] == i)
            temp.pop(pos)
            temp.insert(get_line(pos + n[1]), n)
    zero_index = [i[1] for i in temp].index(0)
    print(sum([temp[get_line(zero_index + 1000)][1], temp[get_line(zero_index + 2000)][1],
               temp[get_line(zero_index + 3000)][1]]))


solve(False)
solve(True)
