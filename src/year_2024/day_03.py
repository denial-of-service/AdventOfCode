import re

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 3)
    regex: str = r'mul\((\d{1,3}),(\d{1,3})\)'
    return sum(int(num_a) * int(num_b) for num_a, num_b in re.findall(regex, puzzle_input))


def part_2() -> int:
    regex: str = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    puzzle_input: str = utils.get_puzzle_input(2024, 3)
    sum_: int = 0
    enabled: bool = True
    for do, dont, num_a, num_b in re.findall(regex, puzzle_input):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            sum_ += int(num_a) * int(num_b)
    return sum_


if __name__ == '__main__':
    print(part_1())
    print(part_2())
