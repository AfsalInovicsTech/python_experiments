
import timeit

def implicit_dict():
    data = {}
    data["a"] = 1
    data["b"] = 2
    data["c"] = 3
    return data


def explicit_dict():
    data = dict()
    data["a"] = 1
    data["b"] = 2
    data["c"] = 3
    return data



time_taken_i = timeit.timeit(implicit_dict)
print("Time taken for implicit: ", time_taken_i)

time_taken_e = timeit.timeit(explicit_dict)
print("Time taken for explicit", time_taken_e)

