import random

import timeit


def sort_function():
   a = list(range(1000_000_0))
   random.shuffle(a)
   return a.sort()



time_taken = timeit.timeit(sort_function, number=1)
print(time_taken)



def sorted_function():
    a = list(range(1000_000_0))
    random.shuffle(a)
    return sorted(a)


time_taken = timeit.timeit(sorted_function, number=1)
print(time_taken)


def sorted_function_under_the_hood():
    a = list(range(1000_000_0))
    random.shuffle(a)
    b = a.copy()
    return b.sort()


time_taken = timeit.timeit(sorted_function_under_the_hood, number=1)
print(time_taken)


import dis

dis.dis(sort_function)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

dis.dis(sorted_function)

print("..............................................................")
