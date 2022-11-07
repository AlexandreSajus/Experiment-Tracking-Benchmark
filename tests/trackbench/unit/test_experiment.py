"""
Tests for the RL Experiment
"""

import pytest_check as check

import stable_baselines3 as sb3
from trackbench.experiment import DQNExperiment


def test_create_DQN():
    """
    Tests if the experiment creates a DQN agent
    """
    experiment = DQNExperiment()
    check.is_instance(experiment.agent, sb3.DQN)
