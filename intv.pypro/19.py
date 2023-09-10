# sum of digits
# 1. while loop
def sum_digits(n):
    temp = n
    sum = 0
    while temp > 0 :
        digit = temp % 10
        sum += digit
        temp //= 10

    print(sum)

number = 123455
sum_digits(number)

# 2. for loop 

def sum_digits2(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
        
    print(sum)

number1 = 123456
sum_digits2(number1)


# ------factorial-------
# 1. for loop
def facto_for(n):
    result = 1
    for i in range(1,n+1):
        result = result * i   #(n+1-i)
    print(result)

facto_for(5)

# 1.2 for loop reverse range
def facto_for2(n):
    result = 1
    for i in range(n,0,-1): 
        result = result * i 
    print(result)

facto_for2(7)

# 2. while loop
def facto_while(n):
    result = 1
    while n > 0 :
        result = result * n
        n -= 1
    print(result)

facto_while(0)

# 3. recursion

def facto_recursion(n):
    if n == 0 or n == 1:
        return 1
    print(n)
    return n*facto_recursion(n-1)

fact = facto_recursion(4)
print(f'Recursion {fact}')