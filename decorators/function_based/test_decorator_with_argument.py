

number = int(input("Enter the number of repetation: "))


def repeat_n_time(ntime):
    def decorated(fun):
        def inner(*args, **kwargs):
            for _ in range(ntime):
                fun(*args, **kwargs)
        return inner
    return decorated


@repeat_n_time(number)
def print_hello_world():
    print("hello world")


print_hello_world()


@repeat_n_time(number)
def say_hello(name):
    print(f"Hello {name}")


say_hello("Python")
