

import timeit


import sys


def print_hello():
    print("print hello")

def stdout_hello():
    sys.stdout.write("stdout hello")



print_hello()
stdout_hello()


time_for_print = timeit.timeit(print_hello, number=1000_000)

time_for_stdout = timeit.timeit(stdout_hello, number=1000_000)


print("Time for print: ", time_for_print)
print("Time for stdout: ", time_for_stdout)
print('.................................')
