import sys
import argparse


def linear_search(
    array: list | dict | str, search_el: object, is_ordered=False
) -> int | None:
    """
    :param array: where you wanna find the value
    :param type: list
    :param search_value: what you wanna find
    :param type: object
    :param is_ordered: if the array is ordered set it to true
    :param type: bool
    :return: Index or None
    :return type: int | None
    """
    are_numbers = True

    for e in array:
        try:
            float(e)
        except Exception as error:
            print(error)
            are_numbers = False

    if is_ordered and are_numbers:
        for i, el in enumerate(array):
            if el == search_el:
                return i
            elif el > search_el:
                break

    else:
        for i, el in enumerate(array):
            if el == search_el:
                return i

    return None


def cli():
    parser = argparse.ArgumentParser(
        __name__,
        description="Find the index of a given value into an iterable",
    )

    parser.add_argument("-a", "--array")
    parser.add_argument("-sv", "--search-value")
    parser.add_argument(
        "--is-ordered", action="store_true", required=False, default=False
    )

    args = parser.parse_args()

    return args


def main(args):

    if args.array and args.search_value:

        array = args.array.split(" ")
        search_el = args.search_value
        is_ordered = args.is_ordered

        i = linear_search(array, search_el, is_ordered)

        print(i)

    else:
        print("insert array and search value")

    return 0


if __name__ == "__main__":
    args = cli()
    exit_code = main(args)
    sys.exit(exit_code)
