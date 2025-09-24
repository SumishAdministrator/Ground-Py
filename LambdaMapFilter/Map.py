"""The map() function in Python is a built-in function that applies a given function to each item 
of an iterable (like a list, tuple, or set) and returns an iterator called a "map object." 
This map object contains the results of applying the function to each element"""

#Example-1
def funct_square(number):
    return number * number

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(funct_square,numbers)
print(list(squared_numbers))

#Example-2
list1 = [1, 2, 3]
list2 = [9, 8, 7]

add_lists = map(lambda x, y: x + y, list1, list2)
print(list(add_lists))