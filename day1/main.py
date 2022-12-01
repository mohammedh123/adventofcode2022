with open('input') as f:
    sorted_elf_total_calories = sorted((sum(map(int, e.split('\n'))) for e in f.read().split('\n\n')), reverse=True)

    print(f'Part 1: {sorted_elf_total_calories[0]}')
    print(f'Part 2: {sum(sorted_elf_total_calories[0:3])}')