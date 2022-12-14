"""Outputs experiment results to TensorBoard"""

import time
from tensorboard import program
from trackbench.experiment import DQNExperiment, PPOExperiment


def run_tensorboard(training_steps: int = 15000) -> str:
    """
    Runs CartPole experiment using TensorBoard.
    """
    # DQN on CartPole
    experiment = DQNExperiment(tensorboard_log="logs/dqn_cartpole")
    print("Training DQN on CartPole...")
    experiment.train(training_steps)

    # PPO on CartPole
    experiment = PPOExperiment(tensorboard_log="logs/ppo_cartpole")
    print("Training PPO on CartPole...")
    experiment.train(training_steps)

    # Launch TensorBoard
    tb = program.TensorBoard()
    tb.configure(argv=[None, "--logdir", "logs"])
    return tb
