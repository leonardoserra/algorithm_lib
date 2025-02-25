import sys
from __init__ import __all__

if __name__ == "__main__":

    print(f"""
        \rHere all the possible algorithm in the library,
        \rType python -m algorithm_lib.[[modulename]] --help
        \rto get specific info
        {"\n- ".join(__all__) + "\n"}
    """)
    sys.exit(0)
