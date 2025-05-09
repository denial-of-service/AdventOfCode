from itertools import combinations

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2020, 1)
    entries: list[int] = list(map(int, puzzle_input.splitlines()))
    for num_a, num_b in combinations(entries, 2):
        if num_a + num_b == 2020:
            return num_a * num_b
    raise Exception()


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2020, 1)
    entries: list[int] = list(map(int, puzzle_input.splitlines()))
    for num_a, num_b, num_c in combinations(entries, 3):
        if num_a + num_b + num_c == 2020:
            return num_a * num_b * num_c
    raise Exception()


if __name__ == '__main__':
    print(part_1())
    print(part_2())
