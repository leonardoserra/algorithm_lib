import sys
import argparse


def linear_search(array, search_el):
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

    args = parser.parse_args()

    return args


def main(args):

    if args.array and args.search_value:

        array = args.array.split(" ")
        search_el = args.search_value

        i = linear_search(array, search_el)

        print(i)

    else:
        print("insert iterable and search value")

    return 0


if __name__ == "__main__":
    args = cli()
    exit_code = main(args)
    sys.exit(exit_code)
