

class Parent:
    public = "public"
    _protected = "protected"
    __private = "private"

    def print_all_members(self):
        print("Public: ", self.public)
        print("protected", self._protected)
        print("private", self.__private)


a = Parent()
print(dir(a))
a.print_all_members()

print(a.public)
print(a._protected)
#print(a.__private)
print(a._Parent__private)
print("stop-----------------------------")


class Child(Parent):
    pass

a = Child()
print(dir(a))
a.print_all_members()

print(a.public)
print(a._protected)
print(a.__private)

