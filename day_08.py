"""
This is Victor Chavanne's answers to day 8 of advent of code 2022 puzzles.
"""


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

    visible_canopy = [[False for _ in x] for x in canopy]

    # Left
    for i, line in enumerate(canopy):
        visible_tree = -1
        for j in range(len(line)):
            if canopy[i][j] > visible_tree:
                visible_tree = canopy[i][j]
                visible_canopy[i][j] = True
    # Right
        visible_tree = -1
        for j in reversed(range(len(line))):
            if line[j] > visible_tree:
                visible_tree = line[j]
                visible_canopy[i][j] = True

    # Top
    for j in range(len(canopy[0])):
        visible_tree = -1
        for i, char in enumerate(canopy):
            if canopy[i][j] > visible_tree:
                visible_tree = canopy[i][j]
                visible_canopy[i][j] = True
    # Bottom
        visible_tree = -1
        for i in reversed(range(len(canopy))):
            if canopy[i][j] > visible_tree:
                visible_tree = canopy[i][j]
                visible_canopy[i][j] = True

    # Sum
    result_list = [sum(x) for x in visible_canopy]
    return sum(result_list)


def get_tree_score(canopy, col, row):
    """This method returns the score of visible tree for one tree.

    :return: The visible tree score.
    :rtype: int
    """

    result = 1
    height = canopy[col][row]

    # Left
    visibles = 0
    for i in range(col-1, -1, -1):
        visibles += 1
        if canopy[i][row] >= height:
            break
    result *= visibles
    # Right
    visibles = 0
    for i in range(col+1, len(canopy[0])):
        visibles += 1
        if canopy[i][row] >= height:
            break
    result *= visibles
    # Top
    visibles = 0
    for j in range(row-1, -1, -1):
        visibles += 1
        if canopy[col][j] >= height:
            break
    result *= visibles
    # Bottom
    visibles = 0
    for j in range(row+1, len(canopy)):
        visibles += 1
        if canopy[col][j] >= height:
            break
    result *= visibles

    return result


def puzzle_two():
    """This method returns the size of the smallest package big enough to free 30000000.

    :return: The size of the package.
    :rtype: int
    """

    canopy = []

    with open("inputs/day_08", "r", encoding="utf_8") as input_file:
        for line in input_file:
            tree_line = []
            for char in line.strip("\n"):
                tree_line.append(int(char))
            canopy.append(tree_line)

    score_canopy = [[0 for _ in x] for x in canopy]

    for i, line in enumerate(canopy):
        for j, _ in enumerate(line):
            score_canopy[i][j] = get_tree_score(canopy, i, j)

    result_list = [max(x) for x in score_canopy]
    return max(result_list)


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
