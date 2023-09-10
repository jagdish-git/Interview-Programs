# 1 ------
def fibonacci(in_a_range):
    a,b = 0,1
    while a < in_a_range:
        yield a
        a, b = b, a+b

f = fibonacci(50)
print(list(f))

# 2 -------
def fibo_in_many(num):
    a,b = 0,1
    c = 0
    while c < num:
        yield a
        a,b = b, a+b
        c += 1
        # yield b
    
f = fibo_in_many(9)
print(list(f))

# 3 -------
def Fibonacci_recursion(n):
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci_recursion(n-1) + Fibonacci_recursion(n-2)

print(Fibonacci_recursion(9))

# 4 -------
def fib_nth(n):
    x,y = 0,1
    c = 0
    while n > c:
          print(x, end=',')
          z = x+y
          x = y
          y = z
          c += 1
    return x

print(fib_nth(9))