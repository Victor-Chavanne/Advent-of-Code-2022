"""
This is Victor Chavanne's answers to day 2 of advent of code 2022 puzzles.
"""


POINTS_DICT = {"move": {"A": 1,
                        "B": 2,
                        "C": 3,
                        "X": 1,
                        "Y": 2,
                        "Z": 3},
               "win": {"A": "B",
                       "B": "C",
                       "C": "A"},
               "lose": {"A": "C",
                        "B": "A",
                        "C": "B"}}


def puzzle_one():
    """This method finds the final score if following the guessed strategy.

    :return: The final score.
    :rtype: int
    """
    points = 0
    with open("inputs/day_02", "r", encoding="utf_8") as input_file:
        for moves in input_file:
            if moves.rstrip("\n") in ["A X", "B Y", "C Z"]:
                points += 3
            elif moves.rstrip("\n") in ["A Y", "B Z", "C X"]:
                points += 6
            elif moves.rstrip("\n") in ["A Z", "B X", "C Y"]:
                points += 0
            # Points for move played
            points += POINTS_DICT["move"][moves[2]]
    return points


def puzzle_two():
    """This method finds the final score if following the real strategy.

    :return: The final score.
    :rtype: int
    """
    points = 0
    with open("inputs/day_02", "r", encoding="utf_8") as input_file:
        for moves in input_file:
            if moves[2] == "X":  # Must lose
                points += 0
                my_move = POINTS_DICT["lose"][moves[0]]
                points += POINTS_DICT["move"][my_move]
            elif moves[2] == "Y":  # Must draw
                points += 3
                my_move = moves[0]
                points += POINTS_DICT["move"][my_move]
            elif moves[2] == "Z":  # Must win
                points += 6
                my_move = POINTS_DICT["win"][moves[0]]
                points += POINTS_DICT["move"][my_move]
    return points


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
