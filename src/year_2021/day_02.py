import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2021, 2)
    horizontal_pos: int = 0
    depth: int = 0

    for line in puzzle_input.splitlines():
        command, units_str = line.split()
        units: int = int(units_str)

        match command:
            case 'forward':
                horizontal_pos += units
            case 'up':
                depth -= units
            case 'down':
                depth += units

    return horizontal_pos * depth


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2021, 2)
    horizontal_pos: int = 0
    depth: int = 0
    aim: int = 0

    for line in puzzle_input.splitlines():
        command, units_str = line.split()
        units: int = int(units_str)

        match command:
            case 'forward':
                horizontal_pos += units
                depth += aim * units
            case 'up':
                aim -= units
            case 'down':
                aim += units

    return horizontal_pos * depth


if __name__ == '__main__':
    print(part_1())
    print(part_2())
