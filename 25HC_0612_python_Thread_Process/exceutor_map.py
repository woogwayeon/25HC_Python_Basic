import random, time, threading
from concurrent.futures import ThreadPoolExecutor

def multipluByTwo(n):
    return 2*n

values = [2,3,4,5,6,7]

def main():
    with ThreadPoolExecutor(max_workers=3) as excutor:
        results = excutor.map(multipluByTwo, values)
        
    for result in results:
        print(result)
        
if __name__ == '__main__':
    main()