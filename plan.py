def shout(text):
    return text.upper()

def wishper(text):
    return text.lower()

def greet(func):
    return func('this is Decorator function calling')


print(greet(shout))
print(greet(wishper))



def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder('15')
 
print(add_15('10'))

import timer
def timer(func):
    def inner():
        print('Before Func')
        func()
        print('After Func')
    return inner

@timer
def machine():
    for i in range(10):
        if i%2 == 0 and i==8:
            print(i)
machine()
