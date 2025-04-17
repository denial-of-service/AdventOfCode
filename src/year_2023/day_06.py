import utils


def part1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2023, 6)
    time_line, distance_line = puzzle_input.splitlines()

    times: list[int] = list(map(int, time_line.split(':')[1].split()))
    distances: list[int] = list(map(int, distance_line.split(':')[1].split()))

    result: int = 1

    for time, record in zip(times, distances):

        min_hold: int = 0
        max_hold: int = -1
        # Find the shortest hold time that beats the record.
        for hold in range(1, time):
            if hold * (time - hold) > record:
                min_hold = hold
                break

        # Find the longest hold time that beats the record.
        for hold in range(time - 1, 0, -1):
            if hold * (time - hold) > record:
                max_hold = hold
                break

        result *= max_hold - min_hold + 1
    return result


def part2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2023, 6)
    time_line, distance_line = puzzle_input.splitlines()

    time: int = int(time_line.split(':')[1].replace(' ', ''))
    record: int = int(distance_line.split(':')[1].replace(' ', ''))

    min_hold: int = 0
    max_hold: int = -1

    # Find the shortest hold time that beats the record.
    for hold in range(1, time):
        if hold * (time - hold) > record:
            min_hold = hold
            break

    # Find the longest hold time that beats the record.
    for hold in range(time - 1, 0, -1):
        if hold * (time - hold) > record:
            max_hold = hold
            break

    return max_hold - min_hold + 1


if __name__ == '__main__':
    print(part1())
    print(part2())
