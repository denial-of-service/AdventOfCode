from src import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2022, 1)
    max_calories: int = 0
    # Split the list of all calories into a list of calories per elf
    calories_list_per_elf: list[str] = puzzle_input.split('\n\n')
    for calories_list in calories_list_per_elf:
        curr_elf_calories = sum(map(int, calories_list.splitlines()))
        max_calories = max(max_calories, curr_elf_calories)
    return max_calories


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2022, 1)
    calories_per_elf: list[int] = []
    # Split the list of all calories into a list of calories per elf
    calories_list_per_elf: list[str] = puzzle_input.split('\n\n')
    for calories_list in calories_list_per_elf:
        curr_elf_calories = sum(map(int, calories_list.splitlines()))
        calories_per_elf.append(curr_elf_calories)
    calories_per_elf.sort(reverse=True)
    return sum(calories_per_elf[:3])


if __name__ == '__main__':
    print(part_1())
    print(part_2())
