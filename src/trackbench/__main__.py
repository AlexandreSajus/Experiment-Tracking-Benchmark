"""
Runs the experiment tracking example using the specified tracking library.
"""

import sys

from trackbench.tensorboard import run_tensorboard
from trackbench.wandb import run_wandb


def main(tracking: str) -> None:
    """
    Runs experiment tracking example using the specified tracking library.

    Args:
        tracking: Tracking library to use
    """
    if tracking == "tensorboard":
        run_tensorboard()
    elif tracking == "wandb":
        run_wandb()
    else:
        print(f"Unknown tracking library: {tracking}")


if __name__ == "__main__":
    main(sys.argv[1])
