"""Stores the experiments used for the benchmark"""

import stable_baselines3 as sb3
import gym


class Experiment:
    """Base class for the experiments"""

    def __init__(self, tensorboard_log: str = None):
        self.agent = None
        self.tensorboard_log = tensorboard_log

    def train(self, training_steps: int = 15000, callbacks: list = None):
        """Trains the agent"""
        self.agent.learn(
            total_timesteps=training_steps,
            tb_log_name=self.tensorboard_log,
            callback=callbacks,
        )

    def set_env(self, env: gym.Env):
        """Sets the environment for the agent"""
        self.agent.set_env(env)


class DQNExperiment(Experiment):
    """DQN experiment"""

    def __init__(self, tensorboard_log: str = None):
        super().__init__(tensorboard_log)
        self.agent = sb3.DQN(
            "MlpPolicy",
            "CartPole-v1",
            verbose=0,
            tensorboard_log=self.tensorboard_log,
        )


class PPOExperiment(Experiment):
    """PPO experiment"""

    def __init__(self, tensorboard_log: str = None):
        super().__init__(tensorboard_log)
        self.agent = sb3.PPO(
            "MlpPolicy",
            "CartPole-v1",
            verbose=0,
            tensorboard_log=self.tensorboard_log,
        )
