import threading, time, random

def myThread(i):
    print(f"Thread {i} started")
    sleepTime = random.randint(2,5)
    time.sleep(sleepTime)
    print(f"------------thread {i} finished")

for i in range(10):
    thread = threading.Thread(target=myThread, args=(i,))
    thread.start()

time.sleep(3)

print(f"Total Active Thread Number : {threading.active_count()}")

