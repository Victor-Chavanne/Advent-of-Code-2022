"""
This is Victor Chavanne's answers to day 4 of advent of code 2022 puzzles.
"""


def puzzle_one():
    """This method finds the number of pair with fully overlapping ranges.

    :return: The number of fully overlapping pairs.
    :rtype: int
    """

    result = 0
    with open("inputs/day_04", "r", encoding="utf_8") as input_file:
        for line in input_file:
            sections = line.split(",")
            range1, range2 = (x.split("-") for x in sections)
            set1 = set(range(int(range1[0]), int(range1[1])+1))
            set2 = set(range(int(range2[0]), int(range2[1])+1))

            if len(set1 - set2) == 0 or len(set2 - set1) == 0:
                result += 1

    return result


def puzzle_two():
    """This method finds the number of pair with overlapping ranges.

    :return: The number of overlapping pairs.
    :rtype: int
    """

    result = 0
    with open("inputs/day_04", "r", encoding="utf_8") as input_file:
        for line in input_file:
            sections = line.split(",")
            range1, range2 = (x.split("-") for x in sections)
            set1 = set(range(int(range1[0]), int(range1[1])+1))
            set2 = set(range(int(range2[0]), int(range2[1])+1))

            if len(set1.union(set2)) != len(set1) + len(set2):
                result += 1

    return result


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
