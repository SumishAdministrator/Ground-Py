"""The destructor in Python is defined by the special method __del__.
It is called when an object is about to be destroyed or garbage collected. """

class Employee:
    # Initialising
    def __init__(self):
        print("Employee created")
    
     # Deleting
    def __del__(self):
        print("Destructor called")

obj_Employee = Employee()
del obj_Employee