"""
Tests for Tensorboard output
"""

import pytest_check as check

from trackbench.tensorboard import run_tensorboard


def test_run_tensorboard():
    """
    Tests if the tensorboard function outputs an url
    """
    url = run_tensorboard()
    check.equal(url[:4], "http")
