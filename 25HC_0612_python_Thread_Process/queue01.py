import threading
import time
import queue

def producer(q, num_items):
    for i in range(num_items):
        item = f"task-{i}"
        q.put(item)
        print(f"producer : put {item}")
        time.sleep(0.2)

def consumer(q):
    while True:
        item = q.get()
        print(f"consumer : got {item}")
        time.sleep(0.5)
        q.task_done()
        print(f"consumer : finished {item}")


my_queue = queue.Queue()
consumer_thread = threading.Thread(target=consumer, args=(my_queue,), daemon=True)
consumer_thread.start()

num_tasks = 5
producer_thread = threading.Thread(target=producer, args=(my_queue, num_tasks), daemon=True)
producer_thread.start()

consumer_thread.join()
producer_thread.join()

print("main : all tasks are finish!")