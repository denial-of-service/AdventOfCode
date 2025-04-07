from src import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 1)
    floor: int = 0
    for char in puzzle_input:
        if char == '(':
            floor += 1
        else:
            floor -= 1
    return floor


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 1)
    floor: int = 0
    for idx, char in enumerate(puzzle_input, start=1):
        if char == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return idx
    return len(puzzle_input)


if __name__ == '__main__':
    print(part1())
    print(part2())
