
import timeit


data = ["a", "b", "c", "d", "e", "f"]



def loop_using_index():
    for index in range(len(data)):
        item = data[index]
        a = item + "test"


def using_pythonic_for_loop():
    for item in data:
        #print(item, end="\r")
        a = item + "test"




time_taken = timeit.timeit(loop_using_index, number=1000_000)
print("Time taken by loop with index", time_taken)

time_taken = timeit.timeit(using_pythonic_for_loop, number=1000_000)
print("Time taken by pythonic for loop ", time_taken)


import dis

dis.dis(loop_using_index)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
dis.dis(using_pythonic_for_loop)
