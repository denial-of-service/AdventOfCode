import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2017, 2)
    result: int = 0

    for line in puzzle_input.splitlines():
        numbers: list[int] = sorted(list(map(int, line.split())))
        # difference between the largest and smallest number
        result += numbers[-1] - numbers[0]

    return result


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2017, 2)
    result: int = 0

    for line in puzzle_input.splitlines():
        numbers: list[int] = sorted(list(map(int, line.split())))
        found: bool = False

        for i, divisor in enumerate(numbers):
            for dividend in numbers[i + 1:]:
                quotient, remainder = divmod(dividend, divisor)
                if not remainder:
                    result += quotient
                    found = True
                    break
            if found:
                break

    return result


if __name__ == '__main__':
    print(part_1())
    print(part_2())
