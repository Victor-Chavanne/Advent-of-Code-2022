"""
This is Victor Chavanne's answers to day 7 of advent of code 2022 puzzles.
"""


def build_tree():
    """This method reads the input file and return a dictionary of file sizes.

    :return: A dictionary of file sizes
    :rtype: dict
    """

    with open("inputs/day_07", "r", encoding="utf_8") as input_file:
        current_directory = ""
        path_sizes = {}
        current_path_list = []
        for line in input_file:
            match [x.strip("\n") for x in line.split(" ")]:
                case ["$", "cd", ".."]:
                    current_directory = "/".join(current_directory.split("/")[:-1]) + "/"
                    current_path_list.pop()
                case ["$", "cd", "/"]:
                    current_directory = "/"
                    current_path_list.append("/")
                case ["$", "cd", dire]:
                    if dire.startswith("/"):
                        current_directory = f"{dire}/"
                        current_path_list = ["/".join(dire.split("/")[:x+1])
                                             for x
                                             in range(len(dire.split("/")))]
                    else:
                        current_directory += f"{dire}/"
                        current_path_list.append(current_directory)
                case ["$", "ls"]:
                    pass
                case ["dir", _]:
                    pass
                case [file_size, _] if file_size[0] in "0123456789":
                    for path in current_path_list:
                        if path not in path_sizes:
                            path_sizes[path] = 0
                        path_sizes[path] += int(file_size)

    return path_sizes


def puzzle_one():
    """This method returns the total sums of directory smaller than 100000.

    :return: The sum of directory sizes
    :rtype: int
    """

    result = 0

    tree = build_tree()
    for value in tree.values():
        if value <= 100000:
            result += value

    return result


def puzzle_two():
    """This method returns the size of the smallest package big enough to free 30000000.

    :return: The size of the package.
    :rtype: int
    """

    tree = build_tree()
    available_space = 70000000 - tree["/"]
    needed_space = 30000000 - available_space

    smallest_sufficient = tree["/"]
    for value in tree.values():
        if needed_space <= value < smallest_sufficient:
            smallest_sufficient = value

    return smallest_sufficient


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
