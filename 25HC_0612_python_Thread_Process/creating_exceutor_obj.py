import time, threading
from concurrent.futures import ThreadPoolExecutor

def myWorker():
    print(f"Executing Work : {threading.current_thread()}")
    result = 0;
    for i in range(10):
        result = result + i # 1부터 9까지 더하기
    time.sleep(1)
    print(f"Task executed : {result}")
    
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executors :
        task1 = executors.submit(myWorker, 10)
        task2 = executors.submit(myWorker, 5)
        task3 = executors.submit(myWorker, 8)