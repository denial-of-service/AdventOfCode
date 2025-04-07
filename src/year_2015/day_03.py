from src import utils


def get_new_pos(char: str, pos: (int, int)) -> (int, int):
    x, y = pos
    match char:
        case '>':
            return x + 1, y
        case '<':
            return x - 1, y
        case '^':
            return x, y + 1
        case 'v':
            return x, y - 1


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 3)
    santa_pos: (int, int) = (0,0)
    visited_houses: set[(int, int)] = {santa_pos}
    for char in puzzle_input:
        santa_pos = get_new_pos(char, santa_pos)
        visited_houses.add(santa_pos)
    return len(visited_houses)


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 3)
    santa_pos: (int, int) = (0,0)
    robot_santa_pos: (int, int) = (0,0)
    visited_houses: set[(int, int)] = {santa_pos}
    for i, character in enumerate(puzzle_input):
        if i % 2 == 0:
            santa_pos = get_new_pos(character, santa_pos)
            visited_houses.add(santa_pos)
        else:
            robot_santa_pos = get_new_pos(character, robot_santa_pos)
            visited_houses.add(robot_santa_pos)
    return len(visited_houses)


if __name__ == '__main__':
    print(part1())
    print(part2())