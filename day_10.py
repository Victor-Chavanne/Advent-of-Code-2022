"""
This is Victor Chavanne's answers to day 10 of advent of code 2022 puzzles.
"""


def puzzle_one():
    """This method returns the sum of the six signal strength.

    :return: The sum of the signal strength
    :rtype: int
    """

    result = 0

    with open("inputs/day_10", "r", encoding="utf_8") as input_file:
        x_register = 1
        cycle = 1
        for line in input_file:
            match line.strip("\n").split(" "):
                case ["noop"]:
                    if (cycle - 20) % 40 == 0:
                        result += x_register * cycle
                    cycle += 1
                case ["addx", value]:
                    if (cycle - 20) % 40 == 0:
                        result += x_register * cycle
                    cycle += 1
                    if (cycle - 20) % 40 == 0:
                        result += x_register * cycle
                    cycle += 1
                    x_register += int(value)

    return result


def puzzle_two():
    """This method prints the images encoded in the inputs
    """
    result = ""

    with open("inputs/day_10", "r", encoding="utf_8") as input_file:
        x_register = 1
        cycle = 1
        for line in input_file:
            match line.strip("\n").split(" "):
                case ["noop"]:
                    if -1 <= ((cycle-1) % 40) - x_register <= 1:
                        result += "#"
                    else:
                        result += "."
                    cycle += 1
                case ["addx", value]:
                    if -1 <= ((cycle-1) % 40) - x_register <= 1:
                        result += "#"
                    else:
                        result += "."
                    cycle += 1
                    if -1 <= ((cycle-1) % 40) - x_register <= 1:
                        result += "#"
                    else:
                        result += "."
                    cycle += 1
                    x_register += int(value)

    result_str = "\n"
    line = ""
    for i, char in enumerate(result):
        line += char
        if len(line) == 40:
            result_str += line
            result_str += "\n"
            line = ""

    return result_str


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
