

def name_exception():
    print(name)

#a = "Test"

def unbound_error():
    a += "hello"
    print(a)


#class A:
#    a = 42
#    b = list(a + i for i in range(10))

# This wont work because the geneate work on
# a separate frame object


a = 1


class B:
    a = 42
    b = list(a + i for i in range(10))

## This work becoasue the  the name a is defined in the outerscope


#name_exception()

#unbound_error()
