import threading, time, random

class SimpleWorker(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        print(f"[starting Thread { self.name }]")
        wait_time = random.uniform(0.1, 0.5)
        time.sleep(wait_time)
        print(f"[Thread : { self.name } finished]")

print("----- Main worker start -----")

thread = []

for i in range(1,11):
    worker = SimpleWorker(name=f"ant-{i}")
    thread.append(worker)

print(f"Ants workter is created")

for i in thread:
    i.start()

for i in thread:
    i.join()
    
print(f"Ants worker is finished")