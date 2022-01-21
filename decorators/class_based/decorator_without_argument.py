

class Repeat5Time:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        for i in range(5):
             self.function()


@Repeat5Time
def print_hello_world():
    print("Hello world")


print_hello_world()
