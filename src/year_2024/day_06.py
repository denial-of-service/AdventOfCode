from dataclasses import dataclass

import utils


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass(frozen=True)
class PositionWithDirection:
    x: int
    y: int
    direction: int


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 6)
    field: list[list[str]] = []
    for line in puzzle_input.splitlines():
        field.append(list(line.strip()))  # Use .strip() to remove any trailing newline characters

    # Find the starting position of the guard
    pos: Position = Position(-1, -1)
    found_starting_pos: bool = False
    for y, row in enumerate(field):
        for x, char in enumerate(row):
            if char == '^':
                pos = Position(x, y)
                found_starting_pos = True
                break
        if found_starting_pos:
            break

    direction: int = 0  # Up
    # Order of movement deltas when turning right
    directions = [(0, -1),  # Up
                  (1, 0),  # Right
                  (0, 1),  # Down
                  (-1, 0)]  # Left
    height: int = len(field)
    width: int = len(field[0])
    visited: set[Position] = set()
    on_field: bool = True

    # Simulate the guard's movements until he leaves the field
    while on_field:
        visited.add(pos)
        dx, dy = directions[direction]
        next_pos: Position = Position(pos.x + dx, pos.y + dy)

        if next_pos.x < 0 or next_pos.x >= width or next_pos.y < 0 or next_pos.y >= height:
            # next position is out of bounds
            on_field = False
        elif field[next_pos.y][next_pos.x] == '#':
            # There's an obstacle, turn right
            direction = (direction + 1) % len(directions)
        else:
            # No obstacle, move forward
            pos = next_pos

    return len(visited)


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 6)
    field: list[list[str]] = []
    for line in puzzle_input.splitlines():
        field.append(list(line.strip()))  # Use .strip() to remove any trailing newline characters

    # Find the starting position of the guard
    start_pos: PositionWithDirection = PositionWithDirection(-1, -1, 0)
    found_starting_pos: bool = False
    for y, row in enumerate(field):
        for x, char in enumerate(row):
            if char == '^':
                start_pos = PositionWithDirection(x, y, 0)
                found_starting_pos = True
                break
        if found_starting_pos:
            break

    curr_pos: Position = Position(start_pos.x, start_pos.y)
    direction: int = 0  # Up
    # Order of movement deltas when turning right
    directions = [(0, -1),  # Up
                  (1, 0),  # Right
                  (0, 1),  # Down
                  (-1, 0)]  # Left
    height: int = len(field)
    width: int = len(field[0])
    visited: set[Position] = set()
    on_field: bool = True

    # Find out which field positions the guard normally visits, use as potential obstacle positions
    while on_field:
        visited.add(curr_pos)
        dx, dy = directions[direction]
        next_pos: Position = Position(curr_pos.x + dx, curr_pos.y + dy)

        if next_pos.x < 0 or next_pos.x >= width or next_pos.y < 0 or next_pos.y >= height:
            # The next position is out of bounds
            on_field = False
        elif field[next_pos.y][next_pos.x] == '#':
            # There's an obstacle, turn right
            direction = (direction + 1) % len(directions)
        else:
            # No obstacle, move forward
            curr_pos = next_pos

    # Find out which obstruction positions cause the guard to walk in circles
    obstruction_positions: int = 0
    for obstruction_candidate in visited:
        if field[obstruction_candidate.y][obstruction_candidate.x] != '.':
            continue
        # Place a new obstacle on the guard's path
        field[obstruction_candidate.y][obstruction_candidate.x] = '#'
        pos: PositionWithDirection = PositionWithDirection(start_pos.x, start_pos.y, start_pos.direction)
        visited_turn_positions: set[PositionWithDirection] = set()
        found_cycle: bool = False
        on_field: bool = True
        while not found_cycle and on_field:
            dx, dy = directions[pos.direction]
            next_pos: PositionWithDirection = PositionWithDirection(pos.x + dx, pos.y + dy, pos.direction)

            if next_pos.x < 0 or next_pos.x >= width or next_pos.y < 0 or next_pos.y >= height:
                # The next position is out of bounds
                on_field = False
            elif field[next_pos.y][next_pos.x] == '#':
                # There's an obstacle, turn right
                if pos in visited_turn_positions:
                    found_cycle = True
                else:
                    visited_turn_positions.add(pos)
                new_direction: int = (pos.direction + 1) % len(directions)
                pos = PositionWithDirection(pos.x, pos.y, new_direction)
            else:
                # No obstacle, move forward
                pos = next_pos
        if found_cycle:
            obstruction_positions += 1
        # reset field
        field[obstruction_candidate.y][obstruction_candidate.x] = '.'
    return obstruction_positions


if __name__ == '__main__':
    print(part1())
    print(part2())
