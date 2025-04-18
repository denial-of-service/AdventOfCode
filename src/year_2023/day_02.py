import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2023, 2)
    cube_limits: dict[str, int] = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_game_ids: int = 0

    for game in puzzle_input.splitlines():
        game_id_section, sets_of_cubes = game.split(': ')
        game_id: int = int(game_id_section.split(' ')[1])
        is_possible: bool = True
        for set_of_cubes in sets_of_cubes.split('; '):
            for cubes in set_of_cubes.split(', '):
                cubes_count_section, color = cubes.split(' ')
                cubes_count: int = int(cubes_count_section)
                if cubes_count > cube_limits[color]:
                    is_possible = False
                    break
            if not is_possible:
                break

        if is_possible:
            sum_of_game_ids += game_id

    return sum_of_game_ids


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2023, 2)
    total_power: int = 0

    for game in puzzle_input.splitlines():
        max_cubes: dict[str, int] = dict.fromkeys(['red', 'green', 'blue'], 0)
        sets_of_cubes = game.split(': ')[1]
        for set_of_cubes in sets_of_cubes.split('; '):
            for cubes in set_of_cubes.split(', '):
                cubes_count_section, color = cubes.split(' ')
                cubes_count: int = int(cubes_count_section)
                max_cubes[color] = max(max_cubes[color], cubes_count)

        total_power += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']

    return total_power


if __name__ == '__main__':
    print(part_1())
    print(part_2())
