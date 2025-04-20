import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2018, 1)
    return sum(map(int, puzzle_input.splitlines()))


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2018, 1)
    frequency_changes: list[int] = list(map(int, puzzle_input.splitlines()))
    frequency: int = 0
    seen_frequencies: set[int] = {frequency}
    while True:
        for frequency_change in frequency_changes:
            frequency += frequency_change
            if frequency in seen_frequencies:
                return frequency
            else:
                seen_frequencies.add(frequency)


if __name__ == '__main__':
    print(part_1())
    print(part_2())
