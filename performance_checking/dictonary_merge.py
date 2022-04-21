
import timeit
from collections import ChainMap
import itertools

a = {str(i): i for i in range(100)}
b = {str(i): i for i in range(101, 200)}


def using_update():
    c = a.copy()
    c.update(b)
    return  c

def using_merge_operator():
    return a | b

def using_unpacking():
    return { **a, **b }

def using_chainmap():
   return ChainMap(a, b)

def using_chain():
   return itertools.chain(a.items(), b.items())


time_taken = timeit.timeit(using_update, number=1000_000)
print("Total time for using_update", time_taken)


time_taken = timeit.timeit(using_merge_operator, number=1000_000)
print("Total time for using merge", time_taken)


time_taken = timeit.timeit(using_unpacking, number=1000_000)
print("Total time for using unpacking", time_taken)

time_taken = timeit.timeit(using_chainmap, number=1000_000)
print("Total time for using chainmap", time_taken)

time_taken = timeit.timeit(using_chain, number=1000_000)
print("Total time for using chain", time_taken)

