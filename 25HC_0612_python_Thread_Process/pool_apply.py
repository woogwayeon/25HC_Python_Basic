import time, multiprocessing
from multiprocessing import Pool

def myTesk(n):
    print(f"Starting : {n} // {multiprocessing.current_process().pid}")
    time.sleep(n)
    print(f"Completed : {n} // {multiprocessing.current_process().pid}")
    return n

def main():
    print("\n\ntesk allocation with map\n\n")
    t0 = time.time()

    with Pool(4) as p:
        result = []
        for i in [4, 3, 2, 1]:
            result.append(p.apply(myTesk, (i,)))
        print(result)
        
    print(f"\n\ntotal time : {time.time() - t0:.2f} sec")


if __name__ == '__main__':
    main()    