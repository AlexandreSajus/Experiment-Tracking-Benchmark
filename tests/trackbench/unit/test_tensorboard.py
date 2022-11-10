"""
Tests for Tensorboard output
"""

import pytest_check as check
from tensorboard import program
from trackbench.tensorboard import run_tensorboard


def test_run_tensorboard():
    """
    Tests if the tensorboard function outputs an url
    """
    tb = run_tensorboard(training_steps=100)
