import functools



def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n-1)


@functools.lru_cache(maxsize=None)
def factorial_with_cache(n):
    if n < 1:
        return 1
    return n * factorial_with_cache(n-1)



def call_factorial():
    factorial(100)

def call_factorial_with_cache():
    factorial_with_cache(100)


import timeit

timetaken = timeit.timeit(call_factorial, number=1000_000)
print("Time taken without cache", timetaken)

timetaken = timeit.timeit(call_factorial_with_cache, number=1000_000)
print("Time taken with cache", timetaken)




