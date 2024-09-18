class C(object):
    def __init__(self):
        self.__x = 120
        x = 17

obj = C()
# print(obj.__x) # AttributeError: 'C' object has no attribute '__x'

def sum(*args):
    r = 0
    for i in args:
        r += i
    return r
# print(sum.__doc__)
# print(sum(1,2,3))
# print(sum(1,2,3,4,5))


str1 = 'Computer'
# print(str1[:8] + 'Science')


def f(values):
    values[1] = 12

v = [1,2,4]
f(v)
# print(v)


arr = [5,16,27,13,8,32]
min = arr[0]
index_min = 0
for i in range(1, len(arr)):
    if arr[i] < min :
        min = arr[i]
        index_min = i
print(index_min)
