import itertools
import sys

from src import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2021, 1)
    measurements: list[int] = list(map(int, puzzle_input.splitlines()))
    increases: int = 0
    for curr, next_ in itertools.pairwise(measurements):
        if curr < next_:
            increases += 1
    return increases


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2021, 1)
    measurements: list[int] = list(map(int, puzzle_input.splitlines()))
    increases: int = 0
    prev_sum: int = sys.maxsize
    for curr, next_, next_next in zip(measurements, measurements[1:], measurements[2:]):
        sum_: int = curr + next_ + next_next
        if prev_sum < sum_:
            increases += 1
        prev_sum = sum_
    return increases


if __name__ == '__main__':
    print(part1())
    print(part2())
