

import timeit
import random

item_set = set(range(1000))
item_list = list(range(1000))

def using_set():
    number = random.randint(1, 2000)
    return number in item_set

def using_list():
    number = random.randint(1, 2000)
    return number in item_list



time_taken = timeit.timeit(using_set, number=1000_000)
print("Time taken by the function using_set is: ", time_taken)

time_taken = timeit.timeit(using_list, number=1000_000)
print("Time taken by the function using_list is: ", time_taken)


import dis

dis.dis(using_set)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

dis.dis(using_list)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
