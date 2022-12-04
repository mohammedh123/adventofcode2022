def pair_fully_contains_pair(p1, p2):
    return p2[0] >= p1[0] and p2[1] <= p1[1]


def pair_partially_contains_pair(p1, p2):
    return p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1]


with open('input') as f:
    section_pairs = []
    for pair in (l.strip().split(',') for l in f):
        section_pairs.append((tuple(map(int, pair[0].split('-'))), tuple(map(int, pair[1].split('-')))))

print(f'Part 1: {sum([1 for p1, p2 in section_pairs if pair_fully_contains_pair(p1, p2) or pair_fully_contains_pair(p2, p1)])}')
print(f'Part 2: {sum([1 for p1, p2 in section_pairs if pair_partially_contains_pair(p1, p2) or pair_partially_contains_pair(p2, p1)])}')