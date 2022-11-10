"""
Runs the experiment tracking example using the specified tracking library.
"""

import time, sys
from trackbench.tensorboard import run_tensorboard


def main(tracking, training_steps=15000) -> int:
    """
    Runs an experiment tracking example using the specified tracking library.
    """
    if tracking == "tensorboard":
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
    else:
        print(f"Unknown tracking library: {tracking}")
        return 0


if __name__ == "__main__":
    n_args = len(sys.argv)
    if n_args <= 1:
        print("Please specify a tracking library")
        print("Usage: python -m trackbench <tracking library> <training steps>")
        sys.exit(1)
    elif n_args == 2:
        main(sys.argv[1])
    elif n_args == 3:
        main(sys.argv[1], training_steps=int(sys.argv[2]))
    else:
        print("Too many arguments")
        print("Usage: python -m trackbench <tracking library> <training steps>")
        sys.exit(1)
