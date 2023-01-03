

import itertools

a = list(range(10))

filter_function = lambda x:x%2==0
selectors = [x%2== 0 for x in range(10)]

def using_filter_method():
     return list(filter(filter_function, a))

def using_compress_method():
    return list(itertools.compress(a, selectors))


import timeit

time_for_filter = timeit.timeit(using_filter_method, number=1000_000)
print("Time for filter method", time_for_filter)

time_for_compress = timeit.timeit(using_compress_method, number=1000_000)
print("Time for compress method", time_for_compress)
