#This code is to use parallel cores from the system for quick program execution

import time
from joblib import Parallel, delayed

my_list = [1,2,3,4]
my_squares = []

#Option-1
"""for i in my_list:
    time.sleep(1)   # Here a delay of 1 sec is intentionally used
    squared = i * i
    my_squares.append(squared)
print(my_squares)"""

#Option-2
def slow_square(i):
    time.sleep(1)
    squared = i * i
    return squared

parallel_obj = Parallel(n_jobs=-1)
my_squares = parallel_obj(delayed(slow_square)(i) for i in my_list)

print(my_squares)
    