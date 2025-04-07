from src import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2019, 1)
    masses: map[int] = map(int, puzzle_input.splitlines())
    total_fuel: int = 0
    for mass in masses:
        total_fuel += mass // 3 - 2
    return total_fuel


def calc_fuel_for_module_and_fuel(mass: int) -> int:
    fuel: int = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + calc_fuel_for_module_and_fuel(fuel)


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2019, 1)
    masses: map[int] = map(int, puzzle_input.splitlines())
    total_fuel: int = 0
    for mass in masses:
        total_fuel += calc_fuel_for_module_and_fuel(mass)
    return total_fuel


if __name__ == '__main__':
    print(part1())
    print(part2())
