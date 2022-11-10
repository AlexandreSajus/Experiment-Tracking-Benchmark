"""
Tests for the RL Experiment
"""

import pytest_check as check

import stable_baselines3 as sb3
from trackbench.experiment import DQNExperiment, PPOExperiment


def test_create_DQN():
    """
    Tests if the experiment creates a DQN agent
    """
    experiment = DQNExperiment()
    check.is_instance(experiment.agent, sb3.DQN)


def test_train_DQN():
    """
    Tests if the experiment runs without TensorBoard
    """
    experiment = DQNExperiment()
    experiment.train(training_steps=100)


def test_tensorboard_DQN():
    """
    Tests if the experiment runs with TensorBoard
    """
    experiment = DQNExperiment(tensorboard_log="logs/dqn_cartpole")
    experiment.train(training_steps=100)


def test_create_PPO():
    """
    Tests if the experiment creates a PPO agent
    """
    experiment = PPOExperiment()
    check.is_instance(experiment.agent, sb3.PPO)


def test_train_PPO():
    """
    Tests if the experiment runs without TensorBoard
    """
    experiment = PPOExperiment()
    experiment.train(training_steps=100)


def test_tensorboard_PPO():
    """
    Tests if the experiment runs with TensorBoard
    """
    experiment = PPOExperiment(tensorboard_log="logs/ppo_cartpole")
    experiment.train(training_steps=100)
