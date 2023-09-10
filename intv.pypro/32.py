def add(func):
    def inner(a,b):
        if a==0 and b == 0:
            print("please change the number")

        func(a,b)
    return inner
 
# def sumx(a,b):
#     print(a+b)

# x = add(sumx)
# x(0,6)



@add
def sum(a,b):
    print(a+b)

sum(0,0)


import time
import math
def calulate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Funtion',func.__name__,'takes', end-start, 'times.')
    return inner

@calulate_time
def fact(num):
    time.sleep(3)
    print(math.factorial(num))

fact(12)