"""Stores the experiments used for the benchmark"""

import stable_baselines3 as sb3


class DQNExperiment:
    """DQN experiment"""

    def __init__(self, tensorboard_log: str = None) -> None:
        self.agent = sb3.DQN(
            "MlpPolicy", "CartPole-v1", verbose=0, tensorboard_log=tensorboard_log
        )
        self.tensorboard_log = tensorboard_log

    def train(self, training_steps=15000) -> None:
        """Trains the agent"""
        self.agent.learn(total_timesteps=training_steps)


class PPOExperiment:
    """PPO experiment"""

    def __init__(self, tensorboard_log: str = None) -> None:
        self.agent = sb3.PPO(
            "MlpPolicy", "CartPole-v1", verbose=0, tensorboard_log=tensorboard_log
        )
        self.tensorboard_log = tensorboard_log

    def train(self, training_steps=15000) -> None:
        """Trains the agent"""
        self.agent.learn(total_timesteps=training_steps)
