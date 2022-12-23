"""
This is Victor Chavanne's answers to day 9 of advent of code 2022 puzzles.
"""


def move_tail(f_knot, b_knot):
    """This method returns the new position of the rope after a head move.

    :param f_knot: The knot to follow
    :type f_knot: lst
    :param b_knot: The knot to move
    :type b_knot: lst
    :return: The new position of the rope
    :rtype: lst
    """

    head = f_knot
    tail = b_knot

    # move tail
    if head[0] == tail[0]:
        if abs(head[1] - tail[1]) > 1:
            tail[1] += (head[1] - tail[1]) / abs(head[1] - tail[1])
    elif head[1] == tail[1]:
        if abs(head[0] - tail[0]) > 1:
            tail[0] += (head[0] - tail[0]) / abs(head[0] - tail[0])
    elif abs(head[1] - tail[1]) + abs(head[0] - tail[0]) > 2:
        tail[1] += (head[1] - tail[1]) / abs(head[1] - tail[1])
        tail[0] += (head[0] - tail[0]) / abs(head[0] - tail[0])

    return [int(tail[0]), int(tail[1])]


def puzzle_one():
    """This method returns the numer of tiles visited by the tail of the bridge.

    :return: The number of tiles visited
    :rtype: int
    """

    head = [0, 0]
    tail = [0, 0]
    tail_position_list = set()

    with open("inputs/day_09", "r", encoding="utf_8") as input_file:
        for line in input_file:
            command = line.strip("\n").split(" ")
            direction = command[0]
            n_iter = int(command[1])

            for _ in range(n_iter):
                # Move head
                if direction == "R":
                    head[0] += 1
                elif direction == "L":
                    head[0] -= 1
                elif direction == "U":
                    head[1] -= 1
                elif direction == "D":
                    head[1] += 1

                tail_position_list.add(tuple(move_tail(head, tail)))

    return len(tail_position_list)


def puzzle_two():
    """This method returns the numer of tiles visited by the long tail of the bridge.

    :return: The number of tiles visited
    :rtype: int
    """

    rope = [[0, 0] for _ in range(10)]
    tail_position_list = set()

    with open("inputs/day_09", "r", encoding="utf_8") as input_file:
        for line in input_file:
            command = line.strip("\n").split(" ")
            direction = command[0]
            n_iter = int(command[1])

            for _ in range(n_iter):
                # Move head
                if direction == "R":
                    rope[0][0] += 1
                elif direction == "L":
                    rope[0][0] -= 1
                elif direction == "U":
                    rope[0][1] -= 1
                elif direction == "D":
                    rope[0][1] += 1

                for i in range(1, len(rope)):
                    rope[i] = move_tail(rope[i-1], rope[i])

                tail_position_list.add(tuple(rope[-1]))

    return len(tail_position_list)


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
