from dis import dis


# Default Argument

def display(f,a=40,b=50,c=30):
    print('f=',f, 'a=',a, 'b=',b,'c=',c)

d = display
d(20)
d(f=300, a=400, b=600, c=100)
d(200,a=400, b=600, c=100)


#def->display(a=40,b=50,c,d=30)// (a=40,b=50,d=30,c) --Non-default argument follows default argument