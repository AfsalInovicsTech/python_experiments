


import timeit




def looping_using_key():
    data = {str(i): i for i in range(20)}
    for key in data:
        #print(data[key])
        a = data[key]



def looping_using_items():
    data = {str(i): i for i in range(20)}
    for key, value in data.items():
        a = value

def looping_using_values():
    data = {str(i): i for i in range(20)}
    for value in data.values():
        a = value





time_taken = timeit.timeit(looping_using_key, number=10000)
print("Time taken using key: ", time_taken)

time_taken = timeit.timeit(looping_using_items, number=10000)

print("Time taken using item: ", time_taken)


time_taken = timeit.timeit(looping_using_values, number=10000)

print("Time taken using value: ", time_taken)


import dis

#dis.dis(looping_using_key)

dis.dis(looping_using_items)
print("..............................")


dis.dis(looping_using_values)

