"""
This is Victor Chavanne's answers to day 8 of advent of code 2022 puzzles.
"""


def puzzle_one():
    """This method returns the numer of visible trees.

    :return: The number of visible trees
    :rtype: int
    """

    result = 0
    canopy = []

    with open("inputs/day_08", "r", encoding="utf_8") as input_file:
        for line in input_file:
            tree_line = []
            for char in line:
                tree_line.append(char)
            canopy.append(tree_line)

    return result


def puzzle_two():
    """This method returns the size of the smallest package big enough to free 30000000.

    :return: The size of the package.
    :rtype: int
    """

    result = 0
    return result


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
