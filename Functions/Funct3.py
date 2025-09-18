# Python program for work on Python Functions

def compute(a, b):
    result = a * b
    if result > 10:
        return result - 3
    else:
        return result + 4
    
print(f"This goes to if block -",compute(5, 4))    
print(f"This goes to else block -",compute(3, 2))

