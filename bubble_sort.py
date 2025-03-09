import sys
import argparse
from . import utils


def bubble_sort(array: list[int]) -> list[int]:
    """
    Implementation of the Bubble Sort Algorithm

    :param array: the list to order.
    :param type: list

    :return: Ordered list in ascendant order
    :return type: list[int] | None
    """
    ordered_list = [*array]

    if utils.are_numbers(ordered_list):
                
        sorted_index = len(ordered_list) - 1
        is_sorted = False

        while not is_sorted:
            is_sorted = True
            for i in range(sorted_index):
                if ordered_list[i] > ordered_list[i + 1]:
                    ordered_list[i], ordered_list[i + 1] = ordered_list[i + 1], ordered_list[i]
                    is_sorted = False
            
            sorted_index -= 1

    return ordered_list


def cli():
    parser = argparse.ArgumentParser(
        __name__,
        description="Given a numeric list it returns the same list with values in ascendant order",
    )

    parser.add_argument("-a", "--array")

    args = parser.parse_args()

    return args


def main(args):

    if args.array:

        array = args.array.split(" ")

        ordered = bubble_sort(array)

        print(ordered)

    else:
        print("insert array")
        return 1

    return 0


if __name__ == "__main__":
    args = cli()
    exit_code = main(args)
    sys.exit(exit_code)
