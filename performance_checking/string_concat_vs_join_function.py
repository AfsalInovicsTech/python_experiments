

import timeit

hello = "hello"
world = "world"
python = "Python"
is_ = "is"
easy = "easy"


def using_join():
    data = [hello, world, python, is_, easy]
    string = " ".join(data)
    return string



def using_concat():
    string = hello + " " + world + " " + python + " " + is_ + " " + easy
    return string


def using_f_string():
    string = f"{hello} {world} {python} {is_} {easy}"
    return string

def using_format():
    string = "{} {} {} {} {}".format(hello, world, python, is_, easy)
    return string



import timeit

using_join_time = timeit.timeit(using_join, number=1000_000)
using_concat_time = timeit.timeit(using_concat, number=1000_000)
using_fstring_time = timeit.timeit(using_f_string, number=1000_1000)

using_format_time = timeit.timeit(using_format, number=1000_1000)


print(using_join_time)
print(using_concat_time)
print(using_fstring_time)

print(using_format_time)

import dis

dis.dis(using_join)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


dis.dis(using_concat)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<,")
dis.dis(using_f_string)

print("................................................................")
dis.dis(using_format)
print("}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}")
