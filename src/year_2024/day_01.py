from collections import Counter

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 1)
    left_nums: list[int] = []
    right_nums: list[int] = []

    for line in puzzle_input.splitlines():
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)

    left_nums.sort()
    right_nums.sort()
    total: int = 0

    for l, r in zip(left_nums, right_nums):
        total += abs(l - r)

    return total


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 1)
    left_nums: list[int] = []
    right_nums: list[int] = []

    for line in puzzle_input.splitlines():
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)

    count_right: Counter = Counter(right_nums)
    total: int = 0

    for l in left_nums:
        total += l * count_right[l]

    return total


if __name__ == '__main__':
    print(part_1())
    print(part_2())
