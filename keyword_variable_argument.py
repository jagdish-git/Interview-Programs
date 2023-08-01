# Keyword Variable Argument



def display(*args, **kwargs): #(**kwargs)
    '''This is keyword variable argument [function.__doc__]'''
    print('args*=', args,'kwargs**=',kwargs, type(kwargs))

d = display
d() #args*= () kwargs**= {} <class 'dict'>
d(3,4) #data*= {} <class 'dict'>
# d(3,4,5) #TypeError: display() takes 2 positional arguments but 9 were given
d(8,9, a=3,b=4,c=5)
# d(8,9, {'a':3,'b':4,'c':5}) #TypeError: display() takes 2 positional arguments but 3 were given
print(d.__doc__)