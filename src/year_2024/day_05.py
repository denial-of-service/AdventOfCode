import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 5)
    rules_section, update_section = puzzle_input.split('\n\n')

    rules: list[tuple[int, int]] = []
    for line in rules_section.splitlines():
        l, r = map(int, line.split('|'))
        rules.append((l, r))

    updates: list[list[int]] = []
    for line in update_section.splitlines():
        updates.append(list(map(int, line.split(','))))

    sum_middle_numbers: int = 0
    for update_section in updates:
        is_valid: bool = True
        for l, r in rules:
            if l in update_section and r in update_section and update_section.index(l) > update_section.index(r):
                is_valid = False
                break

        if is_valid:
            sum_middle_numbers += update_section[len(update_section) // 2]

    return sum_middle_numbers


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 5)
    rules_section, update_section = puzzle_input.split('\n\n')

    rules: list[tuple[int, int]] = []
    for line in rules_section.splitlines():
        l, r = map(int, line.split('|'))
        rules.append((l, r))

    updates: list[list[int]] = []
    for line in update_section.splitlines():
        updates.append(list(map(int, line.split(','))))

    # Find updates that violate rules
    incorrect_updates: list[list[int]] = []
    for update in updates:
        for l, r in rules:
            if l in update and r in update and update.index(l) > update.index(r):
                incorrect_updates.append(update)
                break

    # Swap numbers that violate rules until the no more rules are violated
    for update in incorrect_updates:
        while True:
            is_valid: bool = True
            for l, r in rules:
                if l in update and r in update:
                    l_idx: int = update.index(l)
                    r_idx: int = update.index(r)
                    if l_idx > r_idx:
                        is_valid = False
                        update[l_idx], update[r_idx] = update[r_idx], update[l_idx]

            if is_valid:
                break

    sum_middle_numbers: int = 0
    for update in incorrect_updates:
        sum_middle_numbers += update[len(update) // 2]

    return sum_middle_numbers


if __name__ == '__main__':
    print(part_1())
    print(part_2())
