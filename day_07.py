"""
This is Victor Chavanne's answers to day 7 of advent of code 2022 puzzles.
"""

from pprint import pprint

def build_tree():
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
                        current_path_list = ["/".join(dire.split("/")[:x+1]) for x in range(len(dire.split("/")))]
                    else:
                        current_directory += f"{dire}/"
                        current_path_list.append(current_directory)
                case ["$", "ls"]:
                    pass
                case ["dir", dir_name]:
                    pass
                case [file_size, file_name] if file_size[0] in "0123456789":
                    for p in current_path_list:
                        if p not in path_sizes:
                            path_sizes[p] = 0
                        path_sizes[p] += int(file_size)

    return path_sizes




def puzzle_one():
    """This method looks for start-of-packet marker.
    It return the number of characters needed to be processed to find the first.

    :return: The number of characters processed
    :rtype: int
    """

    result = 0

    tree = build_tree()
    for k in tree.keys():
        if tree[k] <= 100000:
            result += tree[k]

    return result


def puzzle_two():
    """This method looks for end-of-packet marker.
    It return the number of characters needed to be processed to find the first.

    :return: The number of characters processed
    :rtype: int
    """

    result = 0
    return result


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
