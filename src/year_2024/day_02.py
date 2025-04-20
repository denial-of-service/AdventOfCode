import itertools

import utils


def is_sorted_asc(levels: list[int]) -> bool:
    for curr, next_ in itertools.pairwise(levels):
        if curr > next_:
            return False
    return True


def is_sorted_desc(levels: list[int]) -> bool:
    for curr, next_ in itertools.pairwise(levels):
        if curr < next_:
            return False
    return True


def has_only_safe_level_diffs(levels: list[int]) -> bool:
    for curr, next_ in itertools.pairwise(levels):
        diff: int = abs(curr - next_)
        if diff == 0 or diff > 3:
            return False
    return True


def is_safe(levels: list[int]) -> bool:
    return (is_sorted_asc(levels) or is_sorted_desc(levels)) and has_only_safe_level_diffs(levels)


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 2)
    safe_reports: int = 0
    for report in puzzle_input.splitlines():
        levels: list[int] = list(map(int, report.split()))
        if is_safe(levels):
            safe_reports += 1
    return safe_reports


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2024, 2)
    safe_reports: int = 0
    for report in puzzle_input.splitlines():
        levels: list[int] = list(map(int, report.split()))
        # The report may be safe if one level is removed
        for i, _ in enumerate(levels):
            missing_one_level: list[int] = levels.copy()
            del missing_one_level[i]
            if is_safe(missing_one_level):
                safe_reports += 1
                break
    return safe_reports


if __name__ == '__main__':
    print(part_1())
    print(part_2())
