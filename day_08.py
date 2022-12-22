"""
This is Victor Chavanne's answers to day 8 of advent of code 2022 puzzles.
"""

import copy

def puzzle_one():
    """This method returns the numer of visible trees.

    :return: The number of visible trees
    :rtype: int
    """

    canopy = []

    with open("inputs/day_08", "r", encoding="utf_8") as input_file:
        for line in input_file:
            tree_line = []
            for char in line.strip("\n"):
                tree_line.append(int(char))
            canopy.append(tree_line)

    visible_canopy = copy.deepcopy(canopy)

    # Left
    for i, line in enumerate(canopy):
        visible_tree = -1
        for j, char in enumerate(line):
            if char > visible_tree:
                visible_tree = char
                visible_canopy[i][j] = True
            elif visible_canopy[i][j] is not True:
                visible_canopy[i][j] = False

    # Right
    for i, line in enumerate(canopy):
        visible_tree = -1
        for j in range(len(line)-1, -1, -1):
            if line[j] > visible_tree:
                visible_tree = line[j]
                visible_canopy[i][j] = True
            elif visible_canopy[i][j] is not True:
                visible_canopy[i][j] = False

    # Top
    for j in range(len(canopy[0])):
        visible_tree = -1
        for i in range(len(canopy)):
            if char > visible_tree:
                visible_tree = char
                visible_canopy[i][j] = True
            elif visible_canopy[i][j] is not True:
                visible_canopy[i][j] = False

    # Bottom
    for j in range(len(canopy[0])):
        visible_tree = -1
        for i in range(len(canopy)-1, -1, -1):
            if char > visible_tree:
                visible_tree = char
                visible_canopy[i][j] = True
            elif visible_canopy[i][j] is not True:
                visible_canopy[i][j] = False

    # Sum
    result = sum([sum(x) for x in visible_canopy])

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
