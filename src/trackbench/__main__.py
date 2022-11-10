"""
Runs the experiment tracking example using the specified tracking library.
"""

import time
from trackbench.tensorboard import run_tensorboard


def main(training_steps=15000) -> int:
    """
    Runs Tensorboard on CartPole DQN experiment
    """
    print("Training... (this might take some time)")
    tb = run_tensorboard(training_steps=training_steps)
    url = tb.launch()
    print(f"TensorBoard launched at {url}")
    print("Press Ctrl+C to stop TensorBoard")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping TensorBoard")


if __name__ == "__main__":
    main(training_steps=150000)
