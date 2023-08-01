"""Decorators : The decorators are used to modify the behaviour of function or class.
                In decorators, the function are taken as the argument to another function
                and then called inside the wrapper function"""



def hello(func): #step-2
    def inner(): # step-3 ---> inner() is wrapper function
        print('Execute function Before') #step-4.1
        func() # step-5
        print('Execute function After') #step-8
    return inner #step-4

def callble_func(): #step-6
    print("Execute Inside Funcion") #step-7


obj = hello(callble_func) #step-1
# obj() #step-9

@hello
def callble_func_2():
    print('Use the decorator symbole')

# callble_func_2()



print('--------------------------')

import time
import math

# decorator to calculate duration taken by any function.
def calculate_time(func):
	
	# added arguments inside the inner1,if function takes any arguments,can be added like this.
	def inner1(*args, **kwargs):

		# storing time before function execution
		begin = time.time()
		
		func(*args, **kwargs)

		# storing time after function execution
		end = time.time()
		print("Total time taken in : ", func.__name__,end - begin)

	return inner1

# this can be added to any function present,in this case to calculate a factorial
@calculate_time
def factorial(num):

	# sleep 2 seconds because it takes very less time, so that you can see the actual difference
	time.sleep(2)
	print(math.factorial(num))

# calling the function.
factorial(10)


print('------------chain decorator-------------------')

# code for testing decorator chaining
def decor1(func):
    def inner1():
        print('second ----')
        x = func()
        print('second', func.__name__)
        return x * x 
    return inner1

def decor(func):
    def inner():
        print('first----')
        x = func()
        print('first', func.__name__)
        return 2 * x
    return inner


@decor1
@decor
def num():
	return 10

print(num())

# decor1(decor(num))