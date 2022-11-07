"""Outputs experiment results to TensorBoard"""

import time
from tensorboard import program
from trackbench.experiment import DQNExperiment


def run_tensorboard():
    """
    Runs CartPole experiment using TensorBoard.
    """
    # DQN on CartPole
    experiment = DQNExperiment()
    experiment.train()

    # Launch TensorBoard
    tb = program.TensorBoard()
    tb.configure(argv=[None, "--logdir", "logs"])
    url = tb.launch()
    print(f"TensorBoard launched at {url}")
    print("Press Ctrl+C to stop TensorBoard")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        return url
