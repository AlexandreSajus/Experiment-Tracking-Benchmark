"""Outputs experiment results to TensorBoard"""

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
    return url
