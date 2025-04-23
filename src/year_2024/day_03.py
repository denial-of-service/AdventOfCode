import re
from re import Pattern

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 3)
    regex: Pattern[str] = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
    total: int = 0

    for num_a, num_b in regex.findall(puzzle_input):
        total += int(num_a) * int(num_b)

    return total


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 3)
    regex: Pattern[str] = re.compile(r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)")
    total: int = 0
    enabled: bool = True

    for do, dont, num_a, num_b in re.findall(regex, puzzle_input):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            total += int(num_a) * int(num_b)

    return total


if __name__ == '__main__':
    print(part_1())
    print(part_2())
