
import timeit

def using_loop():
    numbers = list(range(50))
    double = []
    for number in numbers:
        double.append(number * 2)
    return double


def using_comprehension():
    numbers = list(range(50))
    return [number * 2 for number in numbers ]



time_taken = timeit.timeit(using_loop, number=1000_000)
print("Time taken for using_loop", time_taken)


time_taken = timeit.timeit(using_comprehension, number=1000_000)
print("Time taken for using_comprehension", time_taken)


import dis

dis.dis(using_loop)

dis.dis(using_comprehension)
