from dataclasses import dataclass

import copy
import re


@dataclass
class Instruction:
    count: int
    src: str
    dst: str


def execute_cratemover_9000_instructions(instructions: list[Instruction], crates: list[str]):
    # Instructions treat crates as a stack
    for i in instructions:
        for _ in range(int(i.count)):
            crates[i.dst].append(crates[i.src].pop())
    return crates


def execute_cratemover_9001_instructions(instructions: list[Instruction], crates: list[str]):
    # Instructions treat crates as a list
    for i in instructions:
        crates[i.dst].extend(crates[i.src][-i.count:])
        del crates[i.src][-i.count:]
    return crates


def generate_crates_str(crates: list[list[str]]):
    # Dicts are traversed in order of insertion in Python 3.7+
    return ''.join(c[-1] for c in crates)


INSTRUCTION_REGEX = re.compile(r'move (\d+) from (\d+) to (\d+)')

with open('input') as f:
    crates_section, instructions_section = f.read().split('\n\n')

crates_grid = [s[1::4] for s in crates_section.split('\n')]
num_crates = len(crates_grid[0])
crates = [None] * num_crates

for x in range(num_crates):
    stack = [crates_grid[y][x] for y in range(-2, -len(crates_grid) - 1, -1) if crates_grid[y][x].strip()]
    idx = int(crates_grid[-1][x]) - 1

    crates[idx] = stack

instructions = []
for instruction in instructions_section.split('\n'):
    count, src, dst = map(int, INSTRUCTION_REGEX.findall(instruction)[0])

    instructions.append(Instruction(count, src - 1, dst - 1))

print(f'Part 1: {generate_crates_str(execute_cratemover_9000_instructions(instructions, copy.deepcopy(crates)))}')
print(f'Part 2: {generate_crates_str(execute_cratemover_9001_instructions(instructions, copy.deepcopy(crates)))}')