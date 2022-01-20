
import time


def stop_watch(start_time=1):
    start_time = start_time
    def inner_function():
        nonlocal start_time
        print(start_time, "s")
        start_time += 1
        time.sleep(1)
    return inner_function


w1 = stop_watch(0)
w2 = stop_watch(100)


from threading import Thread

for i in range(100):
    t1 = Thread(target=w1)
    t1.start()
    t2 = Thread(target=w2)
    t2.start()
    t1.join()
    t2.join()
