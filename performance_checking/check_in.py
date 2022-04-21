


a = list(range(1000))
b = set(range(1000))

def in_using_list():
    return 1 in a

def in_using_set():
    return 1 in b


print(in_using_list())

print(in_using_set())


import timeit

at = timeit.timeit(in_using_list)
print(at)

bt = timeit.timeit(in_using_set)
print(bt)
