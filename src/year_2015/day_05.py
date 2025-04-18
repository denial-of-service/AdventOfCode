from src import utils


def contains_three_vowels(s: str) -> bool:
    count: int = 0
    vowels: list[str] = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char in vowels:
            count += 1
            if count >= 3:
                return True
    return False


def contains_repeated_letters(s: str) -> bool:
    for char, next_char in zip(s, s[1:]):
        if char == next_char:
            return True
    return False


def contains_forbidden_strings(s: str) -> bool:
    forbidden_strings: list[str] = ['ab', 'cd', 'pq', 'xy']
    for char, next_char in zip(s, s[1:]):
        if f'{char}{next_char}' in forbidden_strings:
            return True
    return False


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 5)
    nice_strings_count: int = 0
    for line in puzzle_input.splitlines():
        if contains_three_vowels(line) and contains_repeated_letters(line) and not contains_forbidden_strings(line):
            nice_strings_count += 1
    return nice_strings_count


if __name__ == '__main__':
    print(part_1())
