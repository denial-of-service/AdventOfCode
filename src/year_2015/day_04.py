import hashlib
import itertools

from src import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 4)
    for i in itertools.count(1):
        hash_input: str = f'{puzzle_input}{i}'
        hash_hex: str = hashlib.md5(hash_input.encode()).hexdigest()
        if hash_hex.startswith('00000'):
            return i
    raise Exception()


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 4)
    for i in itertools.count(1):
        hash_input: str = f'{puzzle_input}{i}'
        hash_hex: str = hashlib.md5(hash_input.encode()).hexdigest()
        if hash_hex.startswith('000000'):
            return i
    raise Exception()


if __name__ == '__main__':
    print(part_1())
    print(part_2())
