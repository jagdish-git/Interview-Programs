import time
from multiprocessing import Process


def cal_sqr(list_of_numbers):
    print("Calculate Square Number")
    for n in list_of_numbers:
        time.sleep(5)
        print(f"Square - {n**n}")

def cal_cube(list_of_numbers):
    print("Calculate Cube Number")
    for n in list_of_numbers:
        time.sleep(5)
        print(f"Cube - {n*n*n}")


if __name__ == "__main__":
    array = [2, 3, 5, 6]
    # this happend under two different processes
    process1 = Process(target=cal_sqr, args=(array,))
    process2 = Process(target=cal_cube, args=(array,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()


    print("Execution Done !!" )

