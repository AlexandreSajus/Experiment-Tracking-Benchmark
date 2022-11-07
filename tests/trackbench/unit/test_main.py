"""
Tests main
"""

import pytest_check as check

from trackbench import __main__


def test_main():
    """
    Tests if the main function outputs an url
    """
    url = __main__.main(test=True)
    check.equal(url[:4], "http")
