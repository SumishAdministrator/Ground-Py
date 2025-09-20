# Asserting ZeroDivisionError with Try/except

#import pytest

def div_feat(a, b):
    return a / b

try:
    #def test_div_feat():
    div_feat(4, 0)
    assert False, "Expected ZeroDivisionError"
except ZeroDivisionError:
    assert True #Error occured as expected