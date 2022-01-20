


names = ["Amar", "Akbar", "Antony"]

def hello(name):
    print(f"Hello {name}")

greetings = [lambda :hello(x)  for x in names]

for i in greetings:
    i()


greetings = [lambda x=x:hello(x) for x in names]

for i in greetings:
    i()


# In the abouve example the expected result was Hello Amar, Hello Akbar and Hello Antony
# But the actual result is Hello Antony
# Here in the example the list compherehenc encloses the varialbe x
# When finally executed the value of the x will antony

#in the second list comprehension we are creating a variable for lambda not using closure varualbe for compherehnsion 
#hence it works

from functools import partial


greetings = [partial(hello, x) for x in names]

for i in greetings:
    i()
    print("....................")



def outer_func():
    name = "hi"
    def inner_func():
        print(name)
    return inner_func


a = outer_func()
b = outer_func()
print(a)
print(b)
a()
b()

def outer_func2(name):
   def inner_func():
       print(f"Hello {name}")
   return inner_func

a = outer_func2("test1")
b = outer_func2("test2")
a()
b()

def outer_func3(greeting):
    def inner_func(name):
        return(f"{greeting} {name}")
    return inner_func


hi = outer_func3("Hi")
hello = outer_func3("Hello")

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(hi("Test1"))
print(hello("Test2"))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def outer_func4(name):
    def inner_func():
        return f"Hello {name}"
    return inner_func

a = outer_func4("tsestnam")
print(a())
print(a())


