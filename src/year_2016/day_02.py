from src import utils


def part1() -> str:
    puzzle_input: str = utils.get_puzzle_input(2016, 2)
    keypad: list[list[str]] = [['1', '2', '3'],
                               ['4', '5', '6'],
                               ['7', '8', '9']]
    x: int = 1
    y: int = 1
    code: str = ''
    for line in puzzle_input.splitlines():
        for direction in line:
            match direction:
                case 'U':
                    y = max(0, y - 1)
                case 'L':
                    x = max(0, x - 1)
                case 'D':
                    y = min(2, y + 1)
                case 'R':
                    x = min(2, x + 1)
        code += keypad[y][x]
    return code


def part2() -> str:
    puzzle_input: str = utils.get_puzzle_input(2016, 2)
    keypad: list[list[str]] = [[' ', ' ', '1', ' ', ' '],
                               [' ', '2', '3', '4', ' '],
                               ['5', '6', '7', '8', '9'],
                               [' ', 'A', 'B', 'C', ' '],
                               [' ', ' ', 'D', ' ', ' ']]
    x: int = 0
    y: int = 2
    code: str = ''
    for line in puzzle_input.splitlines():
        for direction in line:
            match direction:
                case 'U':
                    if keypad[y][x] not in {'1', '2', '4', '5', '9'}:
                        y -= 1
                case 'L':
                    if keypad[y][x] not in {'1', '2', '5', 'A', 'D'}:
                        x -= 1
                case 'D':
                    if keypad[y][x] not in {'5', '9', 'A', 'C', 'D'}:
                        y += 1
                case 'R':
                    if keypad[y][x] not in {'1', '4', '9', 'C', 'D'}:
                        x += 1
        code += keypad[y][x]
    return code


if __name__ == '__main__':
    print(part1())
    print(part2())
