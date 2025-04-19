import utils


def part_1() -> int:
    puzzle_input: str = utils.get_puzzle_input(2019, 2)
    op_codes: list[int] = list(map(int, puzzle_input.split(',')))

    # Instructions given in the problem
    op_codes[1] = 12
    op_codes[2] = 2

    for i in range(0, len(op_codes), 4):
        match op_codes[i]:
            case 1:  # Add
                a, b, dest = op_codes[i + 1:i + 4]
                op_codes[dest] = op_codes[a] + op_codes[b]
            case 2:  # Multiply
                a, b, dest = op_codes[i + 1:i + 4]
                op_codes[dest] = op_codes[a] * op_codes[b]
            case 99:  # Halt
                break

    return op_codes[0]


def part_2() -> int:
    puzzle_input: str = utils.get_puzzle_input(2019, 2)
    original_op_codes: list[int] = list(map(int, puzzle_input.split(',')))

    for noun in range(100):
        for verb in range(100):
            op_codes: list[int] = original_op_codes.copy()
            op_codes[1] = noun
            op_codes[2] = verb

            for i in range(0, len(op_codes), 4):
                match op_codes[i]:
                    case 1:  # Add
                        a, b, dest = op_codes[i + 1:i + 4]
                        op_codes[dest] = op_codes[a] + op_codes[b]
                    case 2:  # Multiply
                        a, b, dest = op_codes[i + 1:i + 4]
                        op_codes[dest] = op_codes[a] * op_codes[b]
                    case 99:  # Halt
                        break

            if op_codes[0] == 19690720: # Desired output number.
                return 100 * noun + verb

    raise Exception()


if __name__ == '__main__':
    print(part_1())
    print(part_2())
