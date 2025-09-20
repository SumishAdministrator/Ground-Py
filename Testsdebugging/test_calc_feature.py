# This is the pytest code to test the function add in the calc_feature.py

"""
import calc_feature

def test_add():
    assert calc_feature.add(2,3) == 5        # This will pass
    assert calc_feature.add (3,3) == 5       # This will fail 
"""

from calc_feature import add

def test_add():
    assert add(2,3) == 5        # This will pass
    assert add(3,3) == 5       # This will fail 