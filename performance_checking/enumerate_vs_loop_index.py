
import timeit


data = ["a", "b", "c", "d", "e", "f"]



def loop_using_index():
    for index in range(len(data)):
        item = data[index]
        a = item + "test"


def using_enumerate():
    for index, item in enumerate(data):
        #print(item, end="\r")
        a = item + "test"




time_taken = timeit.timeit(loop_using_index, number=1000_000)
print("Time taken by loop with index", time_taken)

time_taken = timeit.timeit(using_enumerate, number=1000_000)
print("Time taken by enumerate", time_taken)


import dis

dis.dis(loop_using_index)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
dis.dis(using_enumerate)
