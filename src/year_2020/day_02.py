import re
from collections import Counter
from re import Pattern

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2020, 2)
    regex: Pattern[str] = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
    count: int = 0

    for line in puzzle_input.splitlines():
        min_count, max_count, letter, password = regex.match(line).groups()
        letter_count: int = Counter(password)[letter]
        if int(min_count) <= letter_count <= int(max_count):
            count += 1

    return count


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2020, 2)
    regex: Pattern[str] = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
    count: int = 0

    for line in puzzle_input.splitlines():
        pos_1, pos_2, letter, password = regex.match(line).groups()
        first = password[int(pos_1) - 1]
        second = password[int(pos_2) - 1]
        if (first == letter) ^ (second == letter):  # XOR: Exactly one of the two conditions must be true.
            count += 1

    return count


if __name__ == '__main__':
    print(part_1())
    print(part_2())
