with open('input.txt', 'r') as file:
    data = file.read().strip().splitlines()

string = 'XMAS'
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))

total = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] == string[0]:
            for dir in dirs:
                r, c = row, col
                for char in string[1:]:
                    r += dir[0]
                    c += dir[1]
                    if r < 0 or r >= len(data) or c < 0 or c >= len(data[row]) or data[r][c] != char:
                        break
                else:
                    total += 1

print(total)

string = 'MAS'
total = 0
for row in range(len(data)):
    for col in range(len(data[row])):
        if row + 2 < len(data) and col + 2 < len(data[row]):
            if (data[row][col] == string[0] and data[row + 1][col + 1] == string[1] and data[row + 2][col + 2] == string[2]) or (data[row][col] == string[2] and data[row + 1][col + 1] == string[1] and data[row + 2][col + 2] == string[0]):
                if (data[row][col + 2] == string[0] and data[row + 2][col] == string[2]) or (data[row][col + 2] == string[2] and data[row + 2][col] == string[0]):
                    total += 1


print(total)