import itertools
from collections import Counter

import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2018, 2)
    duplicates: int = 0
    triplicates: int = 0

    for line in puzzle_input.splitlines():
        counts: list[int] = list(Counter(line).values())
        if 2 in counts:
            duplicates += 1
        if 3 in counts:
            triplicates += 1

    return duplicates * triplicates


def part_2() -> str:
    puzzle_input: str = utils.get_puzzle_input(2018, 2)
    ids: list[str] = puzzle_input.splitlines()

    for id_a, id_b in itertools.combinations(ids, 2):
        for i, _ in enumerate(id_a):
            # Remove one char at the same pos from both ids.
            trimmed_a: str = id_a[:i] + id_a[i + 1:]
            trimmed_b: str = id_b[:i] + id_b[i + 1:]

            if trimmed_a == trimmed_b:
                return trimmed_a

    raise Exception()


if __name__ == '__main__':
    print(part_1())
    print(part_2())
