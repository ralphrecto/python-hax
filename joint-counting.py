from threading import Lock, Thread

odd_lock = Lock()
even_lock = Lock()

def count(start, stop, acquire_lock, release_lock):
    i = start
    while i <= stop:
        acquire_lock.acquire()
        print(i)
        i += 2
        release_lock.release()


odd_counter = Thread(target=count, args=(1, 100, odd_lock, even_lock))
even_counter = Thread(target=count, args=(2, 100, even_lock, odd_lock))

even_lock.acquire()

odd_counter.start()
even_counter.start()

odd_counter.join()
even_counter.join()
