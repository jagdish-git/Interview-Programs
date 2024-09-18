# FizzBuzz


def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i,'FizzBuzz')
        elif i % 3 == 0:
            print(i,'Fizz')
        elif i % 5 == 0:
            print(i, 'Buzz')
        else:
            print(i)

# fizzbuzz(16)


# 2

def fizzbuzz2(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i,'=','FizzBuzz')
        elif i % 3 == 0:
            print(i,'=','Fizz')
        elif i % 5 == 0:
            print(i, '=','Buzz')

# fizzbuzz2(30)

# dictionary

def dict_fizzbuzz(n):
    dict1 = {3:'fizz', 5:'buzz'}
    for i in range(1,n+1):
        result = ''
        for k,v in dict1.items():
            if i % k == 0:
                result += v
        if not result:
                result = i
        print(result)
            
dict_fizzbuzz(16)

