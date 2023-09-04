import random

a = random.randint(0, 9)

def using_long_if():
    if a == 0:
        return "zero"
    elif a == 1:
        return "one"
    elif a == 2:
        return "two"
    elif a == 3:
        return "three"
    elif a == 4:
        return "four"
    elif a == 5:
        return "five"
    elif a == 6:
        return "six"
    elif a == 7:
        return "seven"
    elif a == 8:
        return "eight"
    elif a == 9:
        return "nine"
    else:
        return "not acceptable"


def using_match():
    match a:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case 3:
            return "three"
        case 4:
            return "four"
        case 5:
            return "five"
        case 6:
            return "six"
        case 7:
            return "seven"
        case 8:
            return "eight"
        case 9:
            return "nine"
        case default:
            return "not acceptable"

map_ = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
def using_dictionary():
    return map_.get(a, "not acceptable")


import timeit 


a = timeit.timeit(using_long_if, number=1000_000)
print(a)

b = timeit.timeit(using_match, number=1000_000)
print(b)

c = b = timeit.timeit(using_dictionary, number=1000_000)
print(c)
