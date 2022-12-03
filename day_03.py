"""
This is Victor Chavanne's answers to day 3 of advent of code 2022 puzzles.
"""


def puzzle_one():
    """This method finds the sum of the priorities of misplaced items.

    :return: The sum of priorities.
    :rtype: int
    """
    char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    with open("inputs/day_03", "r", encoding="utf_8") as input_file:
        for line in input_file:
            cutoff = len(line)//2
            char = "".join(set.intersection(set(line[:cutoff]), set(line[cutoff:])))
            result += char_list.index(char) + 1
    return result


def puzzle_two():
    """This method finds the sum of the priorities of badge items.

    :return: The sum of priorities.
    :rtype: int
    """
    char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    with open("inputs/day_03", "r", encoding="utf_8") as input_file:
        group = []
        for i, line in enumerate(input_file):
            group.append(set(line[:-1]))
            if i % 3 == 2:
                char = "".join(set.intersection(group[0], group[1], group[2]))
                result += char_list.index(char) + 1
                group = []
    return result


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
