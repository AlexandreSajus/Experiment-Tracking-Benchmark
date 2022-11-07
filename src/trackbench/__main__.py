"""
Runs the experiment tracking example using the specified tracking library.
"""

from trackbench.tensorboard import run_tensorboard


def main(training_steps=15000, test=False) -> int:
    """
    Runs Tensorboard on CartPole DQN experiment
    """
    url = run_tensorboard(training_steps=training_steps, test=test)
    return url


if __name__ == "__main__":
    main(training_steps=150000)
