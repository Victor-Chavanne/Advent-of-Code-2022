"""
This is Victor Chavanne's answers to day 6 of advent of code 2022 puzzles.
"""


def puzzle_one():
    """This method looks for start-of-packet marker.
    It return the number of characters needed to be processed to find the first.

    :return: The number of characters processed
    :rtype: int
    """

    result = 0
    with open("inputs/day_06", "r", encoding="utf_8") as input_file:
        line = input_file.read()
        for i in range(len(line)-3):
            if len(set(line[i:i+4])) == 4:
                result = i+4
                break
    return result


def puzzle_two():
    """This method looks for end-of-packet marker.
    It return the number of characters needed to be processed to find the first.

    :return: The number of characters processed
    :rtype: int
    """

    result = 0
    with open("inputs/day_06", "r", encoding="utf_8") as input_file:
        line = input_file.read()
        for i in range(len(line)-13):
            if len(set(line[i:i+14])) == 14:
                result = i+14
    return result


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
