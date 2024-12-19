import time
from multiprocessing import *


sqr_reslut = []
def cal_sqr(list_of_numbers):
    global sqr_reslut
    for n in list_of_numbers:
        print(f"Square - {n**2}")
        sqr_reslut.append(n**2)
    # print("within a process result :",sqr_reslut)

if __name__ == "__main__":
    array = [2, 3, 5, 6]

    process1 = Process(target=cal_sqr, args=(array,))

    process1.start()
    process1.join()

    print("square result : ", sqr_reslut)
    print("Execute Global var Done !!" )

