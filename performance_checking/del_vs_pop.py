import random


def using_pop():
    a = list(range(1000))
    a.pop(500)
    

def using_del():
    a = list(range(1000))
    del a[500]
    




import timeit

time_for_pop = timeit.timeit(using_pop, number=1000_000)
time_for_del = timeit.timeit(using_del, number=1000_000)

print("Time for pop: ", time_for_pop)
print("Time for del: ", time_for_del)


