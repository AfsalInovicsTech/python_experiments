

# from collections import defaultdict


# def using_default_dict():
#     a = defaultdict(list)
#     for i in range(1, 100):
#         a[i].append(i)
#     return a


# print(using_default_dict())


# def using_dict():
#     a = dict()
#     for i in range(1, 100):
#         a.setdefault(i, []).append(i)
#     return a


# print(using_dict())


# import timeit

# time_for_using_default_dict = timeit.timeit(using_default_dict, number=1000_000)
# time_for_using_dict = timeit.timeit(using_dict, number=1000_000)

# print("Time for default dict : ", time_for_using_default_dict)
# print("Time for dict: ", time_for_using_dict)



from collections import defaultdict
  
     
a = defaultdict(lambda: "hello")
a["a"] = 1
a["b"] = 2
  
print(a["a"])
print(a["b"])
print(a["c"])



class ExtendedDict(dict):

    def __init__(self, **kwargs):
        default = kwargs.pop("default")
        super().__init__(kwargs)
        if default:
            self.default = default

    def __missing__(self, key):
        if self.get(key):
            return self.get(key)
        return self.default

a = ExtendedDict(a=1, b=2, default="hello")

print(a)

print(a["a"])
print(a["c"])

