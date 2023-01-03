
import timeit
import copy


a = list(range(100))
q = { i: i for i in range(100) }


def using_list_literal():
    b = list(a)
    return b

def list_copy():
    b = copy.copy(a)
    return b

def using_dict_literal():
    b = dict(q)
    return b

def dict_copy():
    b = copy.copy(q)
    return b



time_for_list_literal = timeit.timeit(using_list_literal, number=1000_000)
print("Time for list literal: ", time_for_list_literal)

time_for_list_copy = timeit.timeit(list_copy, number=1000_000)
print("Time for list copy: ", time_for_list_copy)


time_for_dict_literal = timeit.timeit(using_dict_literal, number=1000_000)
print("Time for dict literal: ", time_for_dict_literal)

time_for_dict_copy = timeit.timeit(dict_copy, number=1000_000)
print("Time for dict copy: ", time_for_dict_copy)
