"""
This is Victor Chavanne's answers to day 11 of advent of code 2022 puzzles.
"""
import copy
from math import floor


def create_monkeys():
    """Create a list of dictionary describing the monkeys

    :return: The list of monkeys as dictionaries
    :rtype: lst
    """
    monkeys = []
    with open("inputs/day_11", "r", encoding="utf_8") as input_file:
        for line in input_file:
            match line.strip().split(" "):
                case ["Monkey", monkey_id]:
                    # Add new monkey to list
                    monkeys.append({"id": monkey_id.rstrip(":")})
                    monkeys[-1]["items_inspected"] = 0
                case ["Starting", "items:", *items]:
                    # add items to last monkey created
                    monkeys[-1]["items"] = [int(item.rstrip(",")) for item in items]
                case ["Operation:", "new", "=", "old", operator, operation_value]:
                    # add operator and operation_value to last monkey created
                    monkeys[-1]["operation"] = operator
                    operation_value = (
                        int(operation_value)
                        if operation_value.isnumeric()
                        else operation_value
                    )
                    monkeys[-1]["operation_value"] = operation_value
                case ["Test:", "divisible", "by", test_value]:
                    # add test value to last monkey created
                    monkeys[-1]["test_value"] = int(test_value)
                case ["If", test_bool, "throw", "to", "monkey", monkey_id]:
                    # throw to correct monkey
                    monkeys[-1][f"{test_bool.rstrip(':').title()}_target"] = monkey_id
    return monkeys


def inspect_and_throw(monkeys, monkey, diviser=3):
    """Loop though items hold by a monkey. Return the holding state after its turn.

    :param monkeys: The list of monkeys dictionaries
    :type monkeys: lst
    :param monkey: The dictionary of the inspected monkey
    :type monkey: dict
    :param diviser: Whether of not to divide concern level by 3
    :type diviser: bool
    :return:
    """
    new_monkeys = copy.deepcopy(monkeys)
    item_inspected = 0

    for item in monkey["items"]:
        # Calculate the new concern value
        new_concern_value = item
        operation_value = (
            item if monkey["operation_value"] == "old" else monkey["operation_value"]
        )
        if monkey["operation"] == "+":
            new_concern_value += operation_value
        elif monkey["operation"] == "-":
            new_concern_value -= operation_value
        elif monkey["operation"] == "/":
            new_concern_value = new_concern_value // operation_value
        elif monkey["operation"] == "*":
            new_concern_value *= operation_value

        if diviser == 3:
            new_concern_value = floor(new_concern_value / diviser)
        else:
            new_concern_value = floor(new_concern_value % diviser)

        # target the correct monkey
        test_concern = new_concern_value % monkey["test_value"] == 0
        target = monkey[f"{test_concern}_target"]

        # throw the item to the correct monkey
        for i, monk in enumerate(monkeys):
            if monk["id"] == target:
                new_monkeys[i]["items"].append(new_concern_value)

        # Increment item counter
        item_inspected += 1

    # Empty item list for current monkey
    for i, monk in enumerate(monkeys):
        if monk["id"] == monkey["id"]:
            new_monkeys[i]["items"] = []
            new_monkeys[i]["items_inspected"] += item_inspected

    return new_monkeys


def puzzle_one():
    """This method returns the product of the number of items inspected by the 2 most productive monkeys.

    :return: The product of the number of items inspected
    :rtype: int
    """

    # Create the monkeys
    monkeys = create_monkeys()

    # Inspect and throw the items
    n_rounds = 20
    for _ in range(n_rounds):
        for j, _ in enumerate(monkeys):
            new_monkeys = inspect_and_throw(monkeys, monkeys[j])
            monkeys = new_monkeys

    # Build inspected items list
    inspected_items = [monkey["items_inspected"] for monkey in monkeys]
    print(inspected_items)

    result = sorted(inspected_items)[-1] * sorted(inspected_items)[-2]
    return result


def puzzle_two():
    """This method returns the product of the number of items inspected by the 2 most productive monkeys.

    :return: The product of the number of items inspected
    :rtype: int
    """

    # Create the monkeys
    monkeys = create_monkeys()

    universal_diviser_list = [monkey["test_value"] for monkey in monkeys]
    diviser = 1
    for num in universal_diviser_list:
        diviser *= num

    # Inspect and throw the items
    n_rounds = 10_000
    for _ in range(n_rounds):
        for j, _ in enumerate(monkeys):
            new_monkeys = inspect_and_throw(monkeys, monkeys[j], diviser=diviser)
            monkeys = new_monkeys

    # Build inspected items list
    inspected_items = [monkey["items_inspected"] for monkey in monkeys]
    print(inspected_items)

    result = sorted(inspected_items)[-1] * sorted(inspected_items)[-2]
    return result


if __name__ == "__main__":
    print(f"Answer to first puzzle is : {puzzle_one()}")
    print(f"Answer to second puzzle is : {puzzle_two()}")
