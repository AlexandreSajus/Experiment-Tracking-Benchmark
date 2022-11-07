"""
Runs the experiment tracking example using the specified tracking library.
"""

import sys


def main(tracking: str) -> int:
    """
    Runs experiment tracking example using the specified tracking library.

    Args:
        tracking: Tracking library to use
    """
    if tracking == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    main(sys.argv[1])
