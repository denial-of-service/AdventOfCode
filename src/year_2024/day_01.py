from collections import Counter

from src import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 1)
    left_nums: list[int] = []
    right_nums: list[int] = []
    for line in puzzle_input.splitlines():
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)
    left_nums.sort()
    right_nums.sort()
    return sum(abs(l - r) for l, r in zip(left_nums, right_nums))


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 1)
    left_nums: list[int] = []
    right_nums: list[int] = []
    for line in puzzle_input.splitlines():
        left, right = map(int, line.split())
        left_nums.append(left)
        right_nums.append(right)
    count_right: Counter = Counter(right_nums)
    return sum(l * count_right[l] for l in left_nums)


if __name__ == '__main__':
    print(part1())
    print(part2())
