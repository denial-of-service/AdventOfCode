import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 2)
    total_wrapping_paper: int = 0

    for line in puzzle_input.splitlines():
        length, width, height = map(int, line.split('x'))  # Convert dimensions to integers
        dimensions: list[int] = sorted([length, width, height])  # Sort dimensions to find the smallest two
        wp_for_box_surface: int = 2 * length * width + 2 * width * height + 2 * height * length
        wp_for_extra_slack: int = dimensions[0] * dimensions[1]
        total_wrapping_paper += wp_for_box_surface + wp_for_extra_slack

    return total_wrapping_paper


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2015, 2)
    total_ribbon_length: int = 0

    for line in puzzle_input.splitlines():
        length, width, height = map(int, line.split('x'))  # Convert dimensions to integers
        dimensions: list[int] = sorted([length, width, height])  # Sort dimensions to find the smallest two
        ribbon_for_box: int = 2 * (dimensions[0] + dimensions[1])
        ribbon_for_bow: int = length * width * height
        total_ribbon_length += ribbon_for_box + ribbon_for_bow

    return total_ribbon_length


if __name__ == '__main__':
    print(part_1())
    print(part_2())
