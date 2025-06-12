from threading import Thread

class myWorkerThread(Thread):
    def __init__(self):
        print("hello world")
        Thread.__init__(self)

    def run(self):
        print("class thread is running")


myThread = myWorkerThread()
print("create my class obj")
myThread.start()
myThread.join()

print("my class Thread finished")