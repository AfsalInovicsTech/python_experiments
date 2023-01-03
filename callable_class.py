

class OrdinaryClass:
    pass

a = OrdinaryClass()
#a()


class CallableClass:

    def __call__(self):
        print("I am callable")

b = CallableClass()


print("Is ordinary class object callable: ", callable(OrdinaryClass()))
print("Is callable class object callable: ", callable(CallableClass()))
