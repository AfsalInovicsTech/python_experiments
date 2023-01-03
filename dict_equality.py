

a = {
    "a": 1,
    "b": 2
}

b = {
    "a": 1,
    "b": 2
}

c = {
    "b": 2,
    "a": 1
}

d = dict(a=1, b=2)
e = dict(b=2, a=1)


print(a == b)

print(b == c)


print(a)
print(b)
print(c)


print(d)
print(e)

print(d==e)
print(d==a)
print(d==c)