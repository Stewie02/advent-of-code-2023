data = open("./real_data.txt").read().splitlines()
raw_seeds, data = [int(x) for x in data[0].split(": ")[1].split(" ")], data[2:]
seed_ranges = [[[raw_seeds[i * 2], raw_seeds[i * 2] + raw_seeds[i * 2 + 1] - 1]] for i in range(len(raw_seeds) // 2)]

maps = []
for line in data:
    if line == "": continue
    if line.count("map:") > 0:
        maps.append([])
        continue
    m = [int(x) for x in line.split(" ")]
    maps[-1].append(m)

def get_locations(map, seed_ranges):
    new_ranges = []
    ranges_to_check_next_iter = seed_ranges
    for line in map:
        dest, src, r = line
        src_end = src + r
        ranges_to_check = ranges_to_check_next_iter
        ranges_to_check_next_iter = []
        for [range_start, range_end] in ranges_to_check:
            
            matches_before = []
            if range_start < src:
                matches_before = [range_start, min(src - 1, range_end)]

            matches_dif = dest - src
            matches = []
            matches_range = range(max(range_start, src), min(range_end, src_end) + 1)
            if len(matches_range) > 0:
                matches = [x + matches_dif for x in [matches_range[0], matches_range[-1]]]

            matches_after = []
            if range_end > src_end:
                matches_after = [max(src_end + 1, range_start), range_end]
            
            if len(matches) > 0: new_ranges.append(matches)
            if len(matches_before) > 0: ranges_to_check_next_iter.append(matches_before)
            if len(matches_after) > 0: ranges_to_check_next_iter.append(matches_after)

    return new_ranges + ranges_to_check_next_iter


smallest_location = -1

for seed_range in seed_ranges:
    location_ranges = seed_range
    for m in maps:
        location_ranges = get_locations(m, location_ranges)
    location = min(min(x) for x in location_ranges)
    if smallest_location == -1 or smallest_location > location:
        smallest_location = location

print(smallest_location)

