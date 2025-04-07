from src import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2017, 1)
    nums: list[int] = list(map(int, puzzle_input))
    total_sum: int = 0
    for num, next_num in zip(nums, nums[1:]):
        if num == next_num:
            total_sum += num
    # the list is circular, so the digit after the last digit is the first digit in the list
    if nums[-1] == nums[0]:
        total_sum += nums[0]
    return total_sum


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2017, 1)
    nums: list[int] = list(map(int, puzzle_input))
    total_sum: int = 0
    digits_count: int = len(nums)
    step: int = digits_count // 2
    for i, _ in enumerate(nums):
        halfway_around_idx: int = (i + step) % digits_count
        if nums[i] == nums[halfway_around_idx]:
            total_sum += nums[i]
    return total_sum


if __name__ == '__main__':
    print(part1())
    print(part2())
