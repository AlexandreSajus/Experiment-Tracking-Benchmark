"""Stores the experiments used for the benchmark"""

import stable_baselines3 as sb3


class DQNExperiment:
    """DQN experiment"""

    def __init__(
        self, training_steps: int = 15000, tensorboard_log: str = None
    ) -> None:
        self.agent = sb3.DQN(
            "MlpPolicy", "CartPole-v1", verbose=0, tensorboard_log=tensorboard_log
        )
        self.tensorboard_log = tensorboard_log
        self.training_steps = training_steps

    def train(self) -> None:
        """Trains the agent"""
        self.agent.learn(total_timesteps=self.training_steps)
