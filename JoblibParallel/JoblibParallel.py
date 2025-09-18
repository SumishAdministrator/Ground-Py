#This code is to use parallel cores from the system for quick program execution

import time

my_list = [1,2,3,4]
my_squares = []

for i in my_list:
    #time.sleep(1)
    squared = i * i
    my_squares.append(squared)

print(my_squares)