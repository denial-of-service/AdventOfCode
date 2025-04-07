from src import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 6)
    field = [[False for _ in range(1000)] for _ in range(1000)]
    for line in puzzle_input.splitlines():
        words: list[str] = line.split()
        command: str
        start_x: int
        start_y: int
        end_x: int
        end_y: int
        if words[0] == 'toggle':
            command = 'toggle'
            start_x, start_y = map(int, words[1].split(','))
            end_x, end_y = map(int, words[3].split(','))
        else:
            command = f'{words[0]} {words[1]}'
            start_x, start_y = map(int, words[2].split(','))
            end_x, end_y = map(int, words[4].split(','))
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                match command:
                    case 'turn on':
                        field[x][y] = True
                    case 'turn off':
                        field[x][y] = False
                    case 'toggle':
                        field[x][y] = not field[x][y]
                    case _:
                        raise Exception()
    # Count how many lights are lit
    return sum(row.count(True) for row in field)


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 6)
    field = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in puzzle_input.splitlines():
        words: list[str] = line.split()
        command: str
        start_x: int
        start_y: int
        end_x: int
        end_y: int
        if words[0] == 'toggle':
            command = 'toggle'
            start_x, start_y = map(int, words[1].split(','))
            end_x, end_y = map(int, words[3].split(','))
        else:
            command = f'{words[0]} {words[1]}'
            start_x, start_y = map(int, words[2].split(','))
            end_x, end_y = map(int, words[4].split(','))
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                match command:
                    case 'turn on':
                        field[x][y] += 1
                    case 'turn off':
                        field[x][y] = max(0, field[x][y] - 1)
                    case 'toggle':
                        field[x][y] += 2
                    case _:
                        raise Exception()
    # Count how many lights are lit
    return sum(sum(row) for row in field)


if __name__ == '__main__':
    print(part1())
    print(part2())
