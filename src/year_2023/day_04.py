from src import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2023, 4)
    total_points: int = 0
    for line in puzzle_input.splitlines():
        _, relevant = line.split(':')
        winning_numbers_side, numbers_i_have_side = relevant.split('|')
        winning_numbers: set[int] = set(map(int, winning_numbers_side.split()))
        numbers_i_have: set[int] = set(map(int, numbers_i_have_side.split()))

        number_of_matches: int = len(winning_numbers.intersection(numbers_i_have))
        if number_of_matches > 0:
            total_points += 2 ** (number_of_matches - 1)
    return total_points


if __name__ == '__main__':
    print(part1())
