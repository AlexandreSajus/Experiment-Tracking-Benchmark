"""
Tests trackbench main function
"""

import pytest_check as check

from trackbench import __main__


def test_wrong_args():
    """
    Tests if the main function raises an error when called with wrong arguments
    """
    check.equal(__main__.main("wrong"), 0)
