import time
from threading import *


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

array = [2, 3, 5, 6, 7]

start_time = time.time()

cal_sqr(array)
cal_cube(array)
    
end_time = time.time()


print(f"Execute Done in : {end_time -  start_time}" )

