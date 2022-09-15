
from functools import cached_property


class A:

   a = 1
   b = 2

   @property
   def normal_property(self):
        #print("Inside normal property")
        return self.a + self.b

   @cached_property
   def cachedproperty(self):
       #print("Inside cached property")
       return self.a + self.b


a = A()
for i in range(5):
    print(a.normal_property)
    print(a.cachedproperty)

def call_normal():
    global a
    return a.normal_property

def call_cached():
    global a
    return a.cachedproperty


import timeit


time_for_normal = timeit.timeit(call_normal, number=1000_000)
print("Time taken for property: ",time_for_normal)

time_for_cached = timeit.timeit(call_cached, number=1000_000)
print("Time taken for cached: ",time_for_cached)


import dis



dis.dis(call_normal)


dis.dis(call_cached)
