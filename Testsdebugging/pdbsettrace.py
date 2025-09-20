# To debug a pytest test using pdb, you can manually insert a breakpoint by adding import pdb; pdb.set_trace() in your test:

import pytest

# Function to be tested
def divide(x,y):
    return x / y

# Test Function added

def test_zero_div():
    import pdb
    pdb.set_trace()
    with pytest.raises(ZeroDivisionError): #Its a context manager which asserts that an Exception named ZeroDivision Error is raised with the execution of its sub code block 
        divide(9,0)


