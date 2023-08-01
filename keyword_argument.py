# Keyword Argument

def display(x,y,z):
    print('x=',x, 'y=',y, 'z=',z)

d = display
d(22,33,44)
d('asdf','asfjdk',32)
d(y=4, x=5, z='fjak')
# d(z=4, y=3, 7) #SyntaxError: positional argument follows keyword argument
