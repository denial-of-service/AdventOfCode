from collections import defaultdict

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 4)
    letters_field: defaultdict[tuple[int, int], str] = defaultdict(str)
    lines: list[str] = puzzle_input.splitlines()
    height: int = len(lines)
    width: int = len(lines[0])

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            letters_field[(x, y)] = char

    # Offsets for checking surrounding cells
    offsets: list[tuple[int, int, int]] = [(-1, -2, -3), (0, 0, 0), (1, 2, 3)]
    xmas_count: int = 0

    # Check each position in the grid
    for x in range(width):
        for y in range(height):
            if letters_field[(x, y)] != 'X':
                continue

            # Check surrounding cells based on offsets
            for xm, xa, xs in offsets:
                for ym, ya, ys in offsets:
                    if (letters_field[(x + xm, y + ym)] == 'M' and
                            letters_field[(x + xa, y + ya)] == 'A' and
                            letters_field[(x + xs, y + ys)] == 'S'):
                        xmas_count += 1

    return xmas_count


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 4)
    letters_field: defaultdict[tuple[int, int], str] = defaultdict(str)
    lines: list[str] = puzzle_input.splitlines()
    height: int = len(lines)
    width: int = len(lines[0])

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            letters_field[(x, y)] = char

    xmas_count: int = 0
    # Check each position in the grid
    for x in range(width):
        for y in range(height):
            if letters_field[(x, y)] != 'A':
                continue

            # Check surrounding cells based on offsets
            if ((letters_field[(x - 1, y - 1)] == 'M' and letters_field[(x + 1, y + 1)] == 'S')
                or (letters_field[(x - 1), y - 1] == 'S' and letters_field[(x + 1, y + 1)] == 'M')) \
                    and ((letters_field[(x + 1, y - 1)] == 'M' and letters_field[(x - 1, y + 1)] == 'S')
                         or (letters_field[(x + 1, y - 1)] == 'S' and letters_field[(x - 1, y + 1)] == 'M')):
                xmas_count += 1

    return xmas_count


if __name__ == '__main__':
    print(part_1())
    print(part_2())
