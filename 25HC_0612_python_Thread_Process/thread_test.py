import threading, time, random

counter = 1
lock = threading.Lock


def inc_worker():
    global counter
    
    lock.acquire()
    
    try:
        while counter<10:
            counter += 1
            print(f"+++ inc_worker { counter }")
            time.sleep(random.randint(0,2))
    finally:
        lock.release()

def dec_worker():
    global counter
    lock.acquire()
    
    try:
        while counter > -10:
            counter -= 1
            print(f"--- dec_worker { counter }")
            time.sleep(random.randint(0,2))
    finally :
        lock.release()

t0 = time.time()
thread1 = threading.Thread(target=inc_worker)
thread2 = threading.Thread(target=inc_worker)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f"Execution Time {time.time()-t0}")