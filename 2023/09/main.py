with open('input.txt') as file:
    LINES = file.read().strip().splitlines()


def sequence_of_diffs(seq):
    for i in range(len(seq) - 1):
        yield seq[i + 1] - seq[i]


part1, part2 = 0, 0
for line in LINES:
    line = list(map(int, line.split()))
    sequences = [line, list(sequence_of_diffs([int(x) for x in line]))]
    while not all(element == 0 for element in sequences[-1]):
        sequences.append(list(sequence_of_diffs(sequences[-1])))

    for seq_i in range(len(sequences) - 1, -1, -1):
        sequences[seq_i - 1].insert(0, sequences[seq_i - 1][0] - sequences[seq_i][0])
        sequences[seq_i - 1].append(sequences[seq_i - 1][-1] + sequences[seq_i][-1])

    part1 += sequences[0][-1]
    part2 += sequences[0][0]

print(part1, part2, sep='\n')
