"""
This is Victor Chavanne's answers to day 5 of advent of code 2022 puzzles.
"""


def stack_reader():
    """This method reads the intial stack order from the input file.

    :return: A list of lists describing the stacks.
    :rtype: list
    """

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    stacks = []
    for i in range(9):
        stack = []
        with open("inputs/day_05", "r", encoding="utf_8") as input_file:
            for line in input_file:
                if line == "\n":
                    break
                char = line[i*4+1]
                if char in letters:
                    stack.insert(0, char)
            stacks.append(stack)
    return stacks


def instructions_reader():
    """This method reads the instructions from the input file.

    :return: A list of instructions.
    :rtype: list
    """
    instructions = []
    with open("inputs/day_05", "r", encoding="utf_8") as input_file:
        for line in input_file:
            if line.startswith("move"):
                instructions.append(line)
    return instructions


def puzzle_one():
    """This method finds the boxes at the top of the stacks.
    The boxes have been shuffled with the 9000.

    :return: The name of the boxes at the top of the stacks.
    :rtype: str
    """

    stacks = stack_reader()
    instructions = instructions_reader()

    for instr in instructions:
        _move, mvcount, _from, mvorig, _to, mvdest = instr.split(" ")
        for i in range(int(mvcount)):
            stacks[int(mvdest)-1].append(stacks[int(mvorig)-1][-1])
            stacks[int(mvorig)-1].pop()

    answer = "".join([x[-1] for x in stacks])
    return answer


def puzzle_two():
    """This method finds the boxes at the top of the stacks.
    The boxes have been shuffled with the 9001.

    :return: The name of the boxes at the top of the stacks.
    :rtype: str
    """

    stacks = stack_reader()
    instructions = instructions_reader()

    for instr in instructions:
        _move, mvcount, _from, mvorig, _to, mvdest = instr.split(" ")
        stacks[int(mvdest)-1] = stacks[int(mvdest)-1] + stacks[int(mvorig)-1][-int(mvcount):]
        for i in range(int(mvcount)):
            stacks[int(mvorig)-1].pop()

    answer = "".join([x[-1] for x in stacks])
    return answer


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
