
#Note: For a unit test in Python, a Single class module is 99% preferred
#pytest tests/test_file.py::test_name. <-- To execute a specific test within that file, append :: and the test name to the file path:


# slicing = [start: stop: step]
''' start: default to 0
    stop default to length_of_list[]]
    step default to 1 '''
# The parameters can be negative or null

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_slicing = numbers[1:4:1]
reversed_number = numbers[9:7:-1]

