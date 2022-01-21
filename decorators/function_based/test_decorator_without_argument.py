



def repeat_5_time(fun):
    def inner():
        for _ in range(5):
            fun()
    return inner


@repeat_5_time
def print_hello_world():
    print("hello world")


print_hello_world()

