class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address



a = Student("Test", 12, "abcd")

print(a.name)
print(a.age)
print(a.address)
#a.abc = "test"
#print(a.abc)
#print(a.__dict__)

class StudentImmutable:
    __slots__ = ["name", "age", "address"]

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address



b = StudentImmutable("Test", 12, "abcd")

print(b.name)
print(b.age)

#print(b.__dict__)
#b.abc = "test"
#print(b.abc)



import sys

from pympler import asizeof

student_array = [a] * 5
print(student_array)
print("Size of student object is: ", asizeof.asizeof(a))

immutable = [b] * 5
print(immutable)
print("Size of studentimmutable object is: ", asizeof.asizeof(b))
