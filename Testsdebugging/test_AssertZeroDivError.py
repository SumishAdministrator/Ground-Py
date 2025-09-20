# This is the pytest code to test the function add in the AssertZeroDiv.py

import pytest
from AssertZeroDivError import div_feat

try:
    def test_div_feat():
        div_feat(4, 0)
        assert False, "Expected ZeroDiveError"
except ZeroDivisionError:
    assert True #Error occured as expected
        