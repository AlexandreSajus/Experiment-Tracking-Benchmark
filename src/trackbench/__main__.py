"""
Runs the experiment tracking example using the specified tracking library.
"""

from trackbench.tensorboard import run_tensorboard


def main() -> int:
    """
    Runs Tensorboard on CartPole DQN experiment
    """
    url = run_tensorboard()
    return url


if __name__ == "__main__":
    main()
