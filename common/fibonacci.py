#>>1
def fibo(n):
    a,b= 0,1
    res = []
    for i in range(n):
        res.append(a)
        a,b = b,a+b
    return res

print(fibo(14)) #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

#>>2
def fibon(n):
    a,b= 0,1
    res = []
    for i in range(n):
        a,b = b,a+b
        res.append(b)
        
    return res

print(fibon(14)) #[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

# >>3 (generator)
def fibonac(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b = b,a+b
        # yield b
    
print(list(fibonac(14)))

#>>4 (3rd var)

def fibonaci(n):
    a=0
    b=1
    res = []
    for i in range(n):
        res.append(a)
        temp = a+b
        a = b
        b = temp
    return res
    
print(fibonaci(14))


# using while loop in a given range

def fibo_while(ranges):
    a = 0
    b = 1
    print(a, end=' ')
    while b < ranges:
        print(b, end=' ')
        c = a+b
        a = b
        b = c
    
fibo_while(50)

print()
# how many numbers you want using while loop

def fibo_while_num(n):
    a,b = 0,1
    count = 0
    while count < n:
        print(a, end=' ')
        a,b = b, a+b
        count += 1

fibo_while_num(15)

print()
# using another for loop 

def fibo_for(n):
    a,b = 0,1
    if n == 1:
        print(a)
    else:
        print(a,b, end = ' ')
        for i in range(2,n):
            a, b = b, a+b
            print(b, end=' ')

fibo_for(12)


print()

# for loop in a given range


def fibo_for_range(ran):
    a,b = 0,1
    print(a, end=' ')
    for i in range(1000):
        print(b, end=' ')
        a,b = b, a+b
        if b > ran:
            break
        
fibo_for_range(200)

# by using RECURSION
print()
print('Recursion')
def fibo_recursion(a,b,n):
    print(a, end=' ')
    a,b = b,a+b
    n = n-1
    if n == 0:
        return n
    return fibo_recursion(a,b, n) 

fibo_recursion(0,1,12)


# 2 recursion (valuable)
print()
def fibonacci_recusion(n):
    if n <= 1:
        return n
    else:
        return (fibonacci_recusion(n-1) + fibonacci_recusion(n-2))

n = 12
if n <=0 :
    print('Invalid')
else:
    for i in range(12):
        print(fibonacci_recusion(i), end=' ')


# Generate an infinite fibonacci series 
# by using Generator(yield)
def fibonacci_infinite():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

f1 = fibonacci_infinite()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))

