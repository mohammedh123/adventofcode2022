import string


def chunkify(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def get_reoccuring_element_from_rucksack(rucksack):
    mid_idx = len(rucksack) // 2
    first_half = set(rucksack[0:mid_idx])
    second_half = set(rucksack[mid_idx:])

    reoccurring_element, = first_half & second_half
    return reoccurring_element


def get_reoccuring_element_from_groups_rucksacks(rucksacks):
    reoccuring_element, = set.intersection(*map(set, rucksacks))
    return reoccuring_element


with open('input') as f:
    rucksacks = [l.strip() for l in f]

type_to_priority = {}
for chr in string.ascii_lowercase:
    type_to_priority[chr] = ord(chr) - ord('a') + 1

for chr in string.ascii_uppercase:
    type_to_priority[chr] = ord(chr) - ord('A') + 27

print(f'Part 1: {sum(type_to_priority[get_reoccuring_element_from_rucksack(r)] for r in rucksacks)}')
print(f'Part 2: {sum(type_to_priority[get_reoccuring_element_from_groups_rucksacks(g)] for g in chunkify(rucksacks, 3))}')