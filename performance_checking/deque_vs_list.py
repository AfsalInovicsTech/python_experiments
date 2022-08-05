

import timeit
import collections
import random


# def using_list_right_insert_and_pop():
#     a = list(range(100))
#     for i in range(100):
#         a.append(i)
#         a.pop()
#     return a


# def using_deque_right_insert_and_pop():
#     a = collections.deque(range(100))
#     for i in range(100):
#         a.append(i)
#         a.pop()
#     return a



# time_taken = timeit.timeit(using_list_right_insert_and_pop, number=1000_000)
# print("Time taken for the function using_list_right_insert_and_pop: ", time_taken)

# time_taken = timeit.timeit(using_deque_right_insert_and_pop, number=1000_000)
# print("Time taken for the function using_deque_right_insert_and_pop: ", time_taken)


# def using_list_left_insert_and_pop():
#     a = list(range(100))
#     for i in range(100):
#         a.insert(0, i)
#         a.pop(0)
#     return a


# def using_deque_left_insert_and_pop():
#     a = collections.deque(range(100))
#     for i in range(100):
#         a.appendleft(1)
#         a.popleft()
#     return a

# time_taken = timeit.timeit(using_list_left_insert_and_pop, number=1000_000)
# print("Time taken for the function using_list_left_insert_and_pop: ", time_taken)

# time_taken = timeit.timeit(using_deque_left_insert_and_pop, number=1000_000)
# print("Time taken for the function using_deque_left_insert_and_pop: ", time_taken)


# def using_list_middle_insert_and_pop():
#     a = list(range(100))
#     for i in range(100):
#         a.insert(50, i)
#         a.pop(50)
#     return a


# def using_deque_middle_insert_and_pop():
#     a = collections.deque(range(100))
#     for i in range(100):
#         a.insert(50, i)
#         del a[50]
#     return a

# time_taken = timeit.timeit(using_list_middle_insert_and_pop, number=1000_000)
# print("Time taken for the function using_list_middle_insert_and_pop: ", time_taken)

# time_taken = timeit.timeit(using_deque_middle_insert_and_pop, number=1000_000)
# print("Time taken for the function using_deque_middle_insert_and_pop: ", time_taken)






def using_list_random_access():
    a = list(range(100))
    for _ in range(10):
        index = random.randint(0, 99)
        b = a[index]


def using_deque_random_access():
    a = collections.deque(range(100))
    for _ in range(10):
        index = random.randint(0, 99)
        b = a[index]

time_taken = timeit.timeit(using_list_random_access, number=1000_000)
print("Time taken for the function using_list_random_access: ", time_taken)

time_taken = timeit.timeit(using_deque_random_access, number=1000_000)
print("Time taken for the function using_deque_random_access: ", time_taken)
