

from functools import partial


def multiply(a, b):
    return a * b


doubler = partial(multiply, 2)
print(doubler)


print(doubler(5))

tripler = partial(multiply, 3)

print(tripler(5))
