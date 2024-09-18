def cube_range(n):
    for i in range(n):
        yield i**3

c = cube_range(10)
print(tuple(c))

def fibo(num):
    a,b = 0,1
    for _ in range(num):
        yield a
        a,b = b, a+b

print(list(fibo(15)))


def gen():
    for i in range(4):
        yield i

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))



# iterator

itr = iter(range(11))
print('iter', next(itr))
print([_ for _ in itr])

st = ['my', 'name','is', 'lakhan']
itr2 = iter(st)
for _ in range(len(st)):
    print(next(itr2))