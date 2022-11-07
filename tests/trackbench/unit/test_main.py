"""
Tests main
"""

import pytest_check as check

from trackbench import __main__


def test_main_function():
    """
    Tests main function in __main__
    """
    check.equal(__main__.main(0), 1)
    check.equal(__main__.main(1), 0)
