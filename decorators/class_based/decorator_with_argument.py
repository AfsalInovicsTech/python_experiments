

class RepeatNTime:
    def __init__(self,n):
        self.n = n

    def __call__(self, function):
        def inner(*args, **kwargs):
            for i in range(self.n):
                function(*args, **kwargs)
        return inner


@RepeatNTime(10)
def print_hello_world(name):
    print(f"Hello world {name}")


print_hello_world("Python")

