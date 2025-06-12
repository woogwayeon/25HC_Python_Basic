import os, math, multiprocessing, time

def childTask():
    print("\n\nstarting my daemon process")
    print(f"child process PID : {multiprocessing.current_process().pid}")
    
    time.sleep(20)
    
    print("\n\ndaemon terminating")
    print(f"main process : {multiprocessing.current_process().pid}")
    
def main():
    myprocess = multiprocessing.Process(target=childTask)
    myprocess.start()
    
    print("\n\nWe can carry on as per usual and out daemon will continue to execute")
    time.sleep(3)
    
    myprocess.terminate()
    print("child process successfully terminated")
    
if __name__ == '__main__':
    main()