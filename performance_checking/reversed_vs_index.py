



def using_reversed():
    a = list(range(500))
    return reversed(a)

def using_slicing():
    a = list(range(500))
    return a[::-1]

def using_reverse():
   a = list(range(500))
   return a.reverse()


import timeit


time_for_reversed = timeit.timeit(using_reversed, number=1000_000)
time_for_reverse = timeit.timeit(using_reverse, number=1000_000)
time_for_slicing = timeit.timeit(using_slicing, number=1000_000)

print("Time taken for using_reversed: ", time_for_reversed)
print("Time taken for using_reverse: ", time_for_reverse)
print("Time taken for using_slicing: ", time_for_slicing)
