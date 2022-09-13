

class WierdInt:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"{self.number}"

    def __add__(self, other):
        return self.number - other.number


a = WierdInt(10)
print(a)

b = WierdInt(5)
print(b)

c = a + b

print(c)
