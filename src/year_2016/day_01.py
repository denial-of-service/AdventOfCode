import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2016, 1)
    # 0 == North, 1 == East, 2 == South, 3 == West
    direction: int = 0
    # [North, East, South, West]
    movement: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x: int = 0
    y: int = 0
    instructions: list[str] = puzzle_input.split(', ')

    for instruction in instructions:
        turn_direction: str = instruction[0]
        distance_in_blocks: int = int(instruction[1:])
        if turn_direction == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        delta_x, delta_y = movement[direction]
        x = x + delta_x * distance_in_blocks
        y = y + delta_y * distance_in_blocks

    return abs(x) + abs(y)


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2016, 1)
    # 0 == North, 1 == East, 2 == South, 3 == West
    direction: int = 0
    # [North, East, South, West]
    movement: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x: int = 0
    y: int = 0
    visited_locations: set[tuple[int, int]] = {(x, y)}
    instructions: list[str] = puzzle_input.split(', ')
    for instruction in instructions:
        turn_direction: str = instruction[0]
        distance_in_blocks: int = int(instruction[1:])
        if turn_direction == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        delta_x, delta_y = movement[direction]
        for _ in range(distance_in_blocks):
            x = x + delta_x
            y = y + delta_y
            pos: (int, int) = (x, y)
            if pos in visited_locations:
                return abs(x) + abs(y)
            else:
                visited_locations.add(pos)
    raise Exception()


if __name__ == '__main__':
    print(part_1())
    print(part_2())
