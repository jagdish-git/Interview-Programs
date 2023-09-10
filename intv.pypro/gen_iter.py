def fibon(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a,b = b, a+b

print(list(fibon(20)))



def simple(n):
    for i in range(n):
        if i%2:
            yield i

s = simple(10)
# print(list(s))


print(next(s))

it = iter(s)
print(list(it))