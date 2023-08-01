# Positional Parameter


def evnod(x):
    if x%2==0:
        return f"{x} is Even Number"
    else:
        return f"{x} is Odd Number"

      
# print(evnod(75))



def fact(n):
    res = 1
    for i in range(1,n+1):
        res = res*i
    return res

# print(fact(5))


def count():
    string = 'abcdefghijklmnopqrstuvwxyzabcefgiouvdcagrejginbfondfjujk'
    c = 0
    for i in string:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            c = c+1
    return c    

# print(count())


def func():
    x = 30
    y = 50
    z = 70
    r = 59
    return z,x,r,y #return a as tuple
t = func()
# print(func())
# print(t[1])


def swap(x=4,y=7):
    x = x+y
    y = x-y
    x = x-y
    return 'x='+str(x), 'y='+str(y)

# print(swap())