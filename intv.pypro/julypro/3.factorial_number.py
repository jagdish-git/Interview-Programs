# 0 ------Lambda
fact_lambda = lambda num : num and num * fact_lambda(num-1) or 1
fact_lambda2 = lambda num : num if num == 1 or num == 0 else num*fact_lambda2(num-1)
fact_lambda3 = lambda num : num*fact_lambda3(num-1) if num > 1 else 1
print(',,,,>>',(fact_lambda3 := lambda num : num*fact_lambda3(num-1) if num > 1 else 1)(5))
print('....>> ', fact_lambda(6))
print('....>> ', fact_lambda2(6))
print('....>> ', fact_lambda3(6))
from functools import reduce
fc = lambda n : reduce(lambda x,y: x*y, range(1,n+1),1)
fc2 = lambda n : reduce(int.__mul__, range(1,n+1),1)
print(fc(7))
print(fc2(7))
# 1 ------
def factorial(num):
    fc = fc2 = 1
    for i in range(1,num+1):
        fc = i * fc

    for i in range(num, 0, -1):
        fc2 *= i
    return fc, fc2

f = factorial(6)
print(f)

# 2 ------
def fact_while(num):
    fact= fact2 = 1
    i = 1
    num1 = num
    while num >= i:
        fact = fact * i
        i += 1
    
    while num1 > 0:
        fact2 *= num1
        num1 -= 1
    return fact, num, fact2

print(fact_while(7))

# 3 ------
def fact_recursive(num):
    if num == 1 or num == 0:
        return 1
    return num*fact_recursive(num-1)

print(fact_recursive(6))

# 4 ------
def factorial_recur(n):
    return n*factorial_recur(n-1) if n > 1 else 1
print(factorial_recur(5))
