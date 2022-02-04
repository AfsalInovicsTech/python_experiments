
import timeit

def implicit_list():
    data = []
    data.append(1)
    data.append(2)
    data.append(3)
    return data


def explicit_list():
    data = list()
    data.append(1)
    data.append(2)
    data.append(3)
    return data





time_taken_i = timeit.timeit(implicit_list, number=1000000)
print("Time taken for implicit is: ", time_taken_i)

time_taken_e = timeit.timeit(explicit_list, number=1000000)
print("Time taken for explicit is: ", time_taken_e)

