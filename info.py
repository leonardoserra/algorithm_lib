import sys
from .__init__ import __all__

if __name__ == "__main__":
    algorithms = [*__all__]

    algorithms.remove('info')
    print("\n\nHere all the possible algorithm in the library,\nType python -m algorithm_lib.{ modulename } --help  \nto get specific info\n\n-" + "\n-".join(algorithms) + "\n")
    sys.exit(0)
