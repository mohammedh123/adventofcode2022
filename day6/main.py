from collections import defaultdict


def get_idx_of_n_unique_chars(n, s):
    l, r = 0, n - 1
    num_unique_chars = 0
    char_count = defaultdict(int)

    for c in s[0:n]:
        if char_count[c] == 0:
            num_unique_chars += 1
        char_count[c] += 1

    while num_unique_chars != n:
        l_char = s[l]
        char_count[l_char] -= 1
        if char_count[l_char] == 0:
            num_unique_chars -= 1

        l += 1
        r += 1

        r_char = s[r]
        if char_count[r_char] == 0:
            num_unique_chars += 1
        char_count[r_char] += 1

    return r + 1


with open('input') as f:
    datastream = f.readline()

print(f'Part 1: {get_idx_of_n_unique_chars(4, datastream)}')
print(f'Part 2: {get_idx_of_n_unique_chars(14, datastream)}')