import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# CPU bound 예제: 소수 판별 (연산 집중)

def cpu_bound_task(n):
    cnt = 0
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
    return cnt == 0

# I/O bound 예제: 파일 읽기 시뮬레이션 (sleep으로 대기)
def io_bound_task(n):
    time.sleep(n)
    return n

PRIMES = [1122725, 11258271, 1199, 10419, 111]
SLEEPS = [1, 1, 1, 1]

def run_cpu_bound():
    print("CPU bound with ProcessPoolExecutor")
    t1 = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(cpu_bound_task, PRIMES))
    print(f"ProcessPool: {time.time() - t1:.2f} sec")
    
    print("Thread bound with ThreadPoolExecutor")
    t2 = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(cpu_bound_task, PRIMES))
    print(f"ThreadPool: {time.time() - t2:.2f} sec")
    
def run_io_bound():
    print("I/O bound with ThreadPoolExecutor")
    t1 = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        list(executor.map(io_bound_task, SLEEPS))
    print(f"ThreadPool: {time.time() -t1:.2f}sec")
    
    print("Process bound with ProcessPoolExecutor")
    t2 = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        list(executor.map(io_bound_task, SLEEPS))
    print(f"ProcessPool: {time.time() -t2:.2f}sec")
    
if __name__ == '__main__':
    run_cpu_bound()
    print("-" * 30)
    run_io_bound()