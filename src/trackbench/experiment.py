"""Stores the experiments used for the benchmark"""

import stable_baselines3 as sb3


class DQNExperiment:
    """DQN experiment"""

    def __init__(self):
        self.agent = sb3.DQN("MlpPolicy", "CartPole-v1", verbose=0)

    def train(self) -> None:
        """Trains the agent"""
        self.agent.learn(total_timesteps=15000)
