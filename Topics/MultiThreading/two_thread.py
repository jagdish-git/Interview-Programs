import time
from threading import Thread


def cal_sqr(list_of_numbers):
    print("Calculate Square Number")
    for n in list_of_numbers:
        time.sleep(0.2)
        print(f"Square ({n}) - {n**2}")

def cal_cube(list_of_numbers):
    print("Calculate Cube Number")
    for n in list_of_numbers:
        time.sleep(0.2)
        print(f"Cube({n}) - {n**3}")

array = [2, 3, 5, 6]

start_time = time.time()

thread1 = Thread(target=cal_sqr, args=(array,))
thread2 = Thread(target=cal_cube, args=(array,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f"Execute Done in : {end_time -  start_time}" )

