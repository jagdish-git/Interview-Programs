# Variable Argument

def display(x,z, *data): #(*args)
    print('x=', x, 'z=',z, 'data*=', data, type(data))

d = display
d(3,4) #data*= () <class 'tuple'>
d(3,4,5)
# d(z=4,x=5,4,5,5) #positional argument follows keyword argument
# d(2,3,4,6, z=4,x=5) #TypeError: display() got multiple values for argument 'z'
d(3,4,5,5,6,7,5,4,6)

print('--------(x,z, *data)-----------------')

def display2(*data, x,z): #(*args)
    print('x=', x, 'z=',z, 'data*=', data)

d2 = display2
d2(x=3,z=4)
d2(3,z=4,x=5)
d2(3,67,78,89,'abc,bcd','cbz',z=4,x=5)


print('--------(*data,x,z)------------------')


def display3(a,b,*data, x,z): #(*args)
    print('x=', x, 'z=',z, 'a,b=',a,b ,'data*=', data)

d3 = display3
d3(3,5, x=6,z=8)
d3(a=5,b=9, x=3,z=30)
# d3(22,33,44,55,a=5,b=9, x=3,z=30) #TypeError: display3() got multiple values for argument 'a'
print('--------(a,b,*data,x,z)--------------')

def display4(*args):
    print(args)

display4('abcd',4,1,3,5,'xyz')