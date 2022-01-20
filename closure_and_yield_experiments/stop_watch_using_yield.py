
import time


def stop_watch(number=0):
    while True:
        number += 1
        reset = yield number
        if reset:
            number = reset
        print(number, "s")
        time.sleep(1)




a = stop_watch(0)

for i in range(100):
    next(a)
    if i%10 == 0:
        a.send(1)
