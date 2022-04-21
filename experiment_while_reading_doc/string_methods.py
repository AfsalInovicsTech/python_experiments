

a = "test"

b = a.center(20, "a")

print(b)

c = a.ljust(20, "b")
print(c)




convertion_map = {
    65+i: 33+i for i in range(92)
}


txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(txt.translate(convertion_map))
