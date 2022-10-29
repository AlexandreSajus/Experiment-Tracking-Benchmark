"""
Runs the experiment tracking example using the specified tracking library.
"""

import sys

from trackbench.tensorboard import run


def main(tracking: str) -> None:
    """
    Runs experiment tracking example using the specified tracking library.

    Args:
        tracking: Tracking library to use
    """
    if tracking == "tensorboard":
        run()


if __name__ == "__main__":
    main(sys.argv[1])
