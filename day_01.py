"""
This is Victor Chavanne's answers to day 1 of advent of code 2022 puzzles.
"""


def get_cal_list():
    """This method loads the inputs for the day, and add each elves' calories together.

    :return: The list of calories carried by each elf.
    :rtype: list
    """

    elf_cals = []
    with open("inputs/day_01", "r", encoding="utf_8") as input_file:
        cal = 0
        for line in input_file:
            if line == "\n":
                elf_cals.append(cal)
                cal = 0
            else:
                cal += int(line[:-1])
    return elf_cals


def puzzle_one():
    """This method finds the amount of calories carried by the elf carrying the most.

    :return: The amount of calories.
    :rtype: int
    """

    elf_cals = get_cal_list()
    return max(elf_cals)


def puzzle_two():
    """This method finds the amount of calories carried by the three elves carrying the most.

    :return: The amount of calories.
    :rtype: int
    """

    elf_cals = get_cal_list()
    elf_cals.sort()
    return sum(elf_cals[-3:])


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
