"""
This is Victor Chavanne's answers to day 12 of advent of code 2022 puzzles.
"""
import string
from pprint import pprint

def import_elevation_map():
    elevation_list = [letter for letter in string.ascii_lowercase]
    elevation_map = []
    start_pos = []
    end_pos = []

    with open("inputs/day_12", "r", encoding="utf_8") as input_file:
        for y, line in enumerate(input_file):
            clean_line = line.strip()
            elevation_line = []
            for x, char in enumerate(clean_line):
                if char == "S":
                    start_pos = (x, y)
                    elevation_line.append(0)
                elif char == "E":
                    end_pos = (x, y)
                    elevation_line.append(26)
                else:
                    elevation_line.append(elevation_list.index(char))

            elevation_map.append(elevation_line)

    return elevation_map, start_pos, end_pos

def get_possible_connections(map, dist_map, node):
    x, y = node
    possible_connections = []

    if x-1 >= 0:
        if map[y][x-1] - map[y][x] <= 1 and dist_map[y][x-1] > dist_map[y][x] + 1:
            possible_connections.append((x-1, y))
    if x+1 < len(map[0]):
        if map[y][x+1] - map[y][x] <= 1 and dist_map[y][x+1] > dist_map[y][x] + 1:
            possible_connections.append((x+1, y))
    if y-1 >= 0:
        if map[y-1][x] - map[y][x] <= 1 and dist_map[y-1][x] > dist_map[y][x] + 1:
            possible_connections.append((x, y-1))
    if y+1 < len(map):
        if map[y+1][x] - map[y][x] <= 1 and dist_map[y+1][x] > dist_map[y][x] + 1:
            possible_connections.append((x, y+1))

    return possible_connections


def pathfinder(start, end, map):
    """finds a path from start to goal.

    :param start: Starting position
    :param end: Goal position
    :param map:
    :return:
    """

    dist_map = [[1000 for _ in line] for line in map]
    dist_map[start[1]][start[0]] = 0

    nodes_to_inspect = [start]

    while len(nodes_to_inspect) != 0:
        focus_node = nodes_to_inspect[0]

        #if focus_node == end:
            #for line in dist_map:
                #print(line)
            #return dist_map[focus_node[1]][focus_node[0]]

        focus_value = dist_map[focus_node[1]][focus_node[0]]
        for node in get_possible_connections(map, dist_map, focus_node):
            nodes_to_inspect.append(node)
            dist_map[node[1]][node[0]] = focus_value + 1
        nodes_to_inspect.pop(0)

    for line in dist_map:
        print(line)
    return dist_map[end[1]][end[0]]

def puzzle_one():
    """This method returns the product of the number of items inspected by the 2 most productive monkeys.

    :return: The product of the number of items inspected
    :rtype: int
    """

    map, start, end = import_elevation_map()
    result = pathfinder(start, end, map)
    return result


def puzzle_two():
    """This method returns the product of the number of items inspected by the 2 most productive monkeys.

    :return: The product of the number of items inspected
    :rtype: int
    """

    result = 0
    return result


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
