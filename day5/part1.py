
data = open("./data.txt").read().splitlines()
seeds, data = [int(x) for x in data[0].split(": ")[1].split(" ")], data[2:]

maps = []
for line in data:
    if line == "": continue
    if line.count("map:") > 0:
        maps.append([])
        continue
    m = [int(x) for x in line.split(" ")]
    maps[-1].append(m)


def get_location(map, seed):
    for line in map:
        dest, src, range = line
        src_end = src + range
        if src <= seed < src_end:
            return seed + (dest - src)
    return seed


smallest_location = -1

for seed in seeds:
    location = seed
    for m in maps:
        location = get_location(m, location)
    if smallest_location == -1 or smallest_location > location:
        smallest_location = location

print(smallest_location)

