import itertools

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 7)
    total: int = 0
    operands = ['+', '*']
    for line in puzzle_input.splitlines():
        test_value_section, numbers_section = line.split(':')
        test_value: int = int(test_value_section)
        numbers: list[int] = list(map(int, numbers_section.split()))
        # Generate all combinations of operands
        operands_combinations = itertools.product(operands, repeat=len(numbers) - 1)
        for operands_combination in operands_combinations:
            sum_: int = numbers[0]
            for operand, num in zip(operands_combination, numbers[1:]):
                if sum_ > test_value:
                    break
                match operand:
                    case '+':
                        sum_ += num
                    case '*':
                        sum_ *= num
            if sum_ == test_value:
                total += test_value
                break
    return total


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 7)
    total: int = 0
    operands = ['+', '*', '||']
    for line in puzzle_input.splitlines():
        test_value_section, numbers_section = line.split(':')
        test_value: int = int(test_value_section)
        numbers: list[int] = list(map(int, numbers_section.split()))
        # Generate all combinations of operands
        operands_combinations = itertools.product(operands, repeat=len(numbers) - 1)
        for operands_combination in operands_combinations:
            sum_: int = numbers[0]
            for operand, num in zip(operands_combination, numbers[1:]):
                if sum_ > test_value:
                    break
                match operand:
                    case '+':
                        sum_ += num
                    case '*':
                        sum_ *= num
                    case '||':
                        # String concatenation operator
                        sum_ = int(str(sum_) + str(num))
            if sum_ == test_value:
                total += test_value
                break
    return total


if __name__ == '__main__':
    print(part_1())
    print(part_2())
