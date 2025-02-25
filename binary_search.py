import sys
import argparse
import utils


def binary_search(array: list | str, search_el: str) -> int | float | None:
    """
    Implementation of the Binary Search Algorithm

    :param array: where you wanna find the value
    :param type: list
    :param search_value: what you wanna find
    :param type: object

    :return: Index or None
    :return type: int | None
    """

    if utils.are_numbers(array) and search_el.isdigit():

        search_el = float(search_el)
        head = 0
        tail = len(array) - 1
        middle = (tail - head) // 2
        
        while head <= tail:
            value = array[middle]
            print(value)

            if search_el == value:
                return value

            elif search_el > value:
                head = middle + 1

            elif search_el < value:
                tail = middle - 1
    else:
        print("To work, all the elements and the search_el must be numbers")

    return None


def cli():
    parser = argparse.ArgumentParser(
        __name__,
        description="Find the index of a given value into an iterable, using the binary search algorithm",
    )

    parser.add_argument("-a", "--array")
    parser.add_argument("-sv", "--search-value")

    args = parser.parse_args()

    return args


def main(args):

    if args.array and args.search_value:

        array = args.array.split(" ")
        search_el = args.search_value

        i = binary_search(array, search_el)

        print(i)

    else:
        print("insert array and search value")
        return 1

    return 0


if __name__ == "__main__":
    args = cli()
    exit_code = main(args)
    sys.exit(exit_code)
