

import timeit
import collections


def using_list_right_insert_and_pop():
    a = []
    for i in range(100):
        a.append(i)
        a.pop()
    return a


def using_deque_right_insert_and_pop():
    a = collections.deque()
    for i in range(100):
      a.append(i)
      a.pop()
    return a



time_taken = timeit.timeit(using_list_right_insert_and_pop, number=1000_000)
print(time_taken)

time_taken = timeit.timeit(using_deque_right_insert_and_pop, number=1000_000)
print(time_taken)


def using_list_left_insert_and_pop():
    a = []
    for i in range(100):
        a.insert(0, i)
        a.pop(0)
    return a


def using_deque_left_insert_and_pop():
    a = collections.deque()
    for i in range(100):
      a.appendleft(i)
      a.popleft()
    return a



time_taken = timeit.timeit(using_list_left_insert_and_pop, number=1000_000)
print(time_taken)

time_taken = timeit.timeit(using_deque_left_insert_and_pop, number=1000_000)
print(time_taken)
