
data = open("data.txt").read().splitlines()


def get_next(line):
    values = [int(x) for x in line.split()]
    sequences = [values]
    while any(x != 0 for x in sequences[-1]):
        new = []
        for i in range(1, len(sequences[-1])):
            new.append(sequences[-1][i] - sequences[-1][i - 1])
        sequences.append(new)
    for i in range(len(sequences) - 2, -1, -1):
        num = sequences[i + 1][-1] + sequences[i][-1]
        sequences[i].append(num)
    return sequences[0][-1]

ans = sum(get_next(x) for x in data)
print(ans)


