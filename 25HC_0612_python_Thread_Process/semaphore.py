import threading, time, random

parking_lot = threading.Semaphore(3)

def car_parking(car_id):
    print(f"{ car_id } : finding.. parking zone")
    parking_lot.acquire()
    print(f"{ car_id } : found parking zone! ( left : {parking_lot._value} )")
    
    time.sleep(random.randint(1,3))
    print(f"{ car_id } : lets go")

    parking_lot.release()
    print(f"{ car_id } left : {parking_lot._value}")

cars = []

for i in range(1, 11):
    car = threading.Thread(target=car_parking, args=(i,))
    cars.append(car)
    car.start()

for i in cars:
    i.join()

print("All parking process is done")