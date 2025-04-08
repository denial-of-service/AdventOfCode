import re
from re import Pattern

import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2023, 1)
    sum_: int = 0
    pattern = re.compile(r'\d')
    for line in puzzle_input.splitlines():
        digits = pattern.findall(line)
        if digits:
            first_digit: str = digits[0]
            last_digit: str = digits[-1]
            sum_ += int(f'{first_digit}{last_digit}')
    return sum_


def parse_number_str(number_str: str) -> str:
    match number_str:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'
        case _:
            return number_str


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2023, 1)
    sum_: int = 0
    numbers: str = 'one|two|three|four|five|six|seven|eight|nine'
    pattern: Pattern[str] = re.compile(rf'\d|{numbers}')
    # str[::-1] reverses the str
    reversed_pattern: Pattern[str] = re.compile(rf'\d|{numbers[::-1]}')
    for line in puzzle_input.splitlines():
        first_match: str = pattern.search(line).group()
        first_digit: str = parse_number_str(first_match)
        # Searching from start to end doesn't work if numbers overlap.
        # E.g. 'twone' would incorrectly return 'two' instead of 'one'.
        last_match: str = reversed_pattern.search(line[::-1]).group()
        last_digit: str = parse_number_str(last_match[::-1])
        sum_ += int(f'{first_digit}{last_digit}')
    return sum_


if __name__ == '__main__':
    print(part1())
    print(part2())
