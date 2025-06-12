import time, timeit, random
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os, math

PRIMES = [
    112272535095293,
    112582805942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
    112272535095293,
    112582805942171,
    112272535095293,
    115280095190773,
    115797848077099,
]

def is_prime(n):
    if n % 2 == 0 :
        return False
    
    sqrt_n = int(math.floor(math.sqrt(n)))
    
    for i in range(3, sqrt_n+1,2):
    
        if n % i == 0:
            return False
        return True
    
    
def main():
    t2 = timeit.default_timer()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f"{number} is prime : {prime}")
    
    print(f"\n\nT2 : {timeit.default_timer() - t2} Secondes needed for ThreadPoolExecutor")
    t1 = timeit.default_timer()
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f"{number} is prime : {prime}")
        
    print(f"\n\nT1 : {timeit.default_timer() - t1} Secondes needed for ProcessPoolExecutor\n\n")
    
    
    
if __name__ == '__main__':
    main()