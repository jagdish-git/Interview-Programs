def flower(func):
    def smell():
        print(func())
        return 'SMELL'

    print('Flower')
    return smell


def fruit():
    print('Print Fruit')
    return 'Fruit'

@flower
def root():
    print('Root')
    return 'Return Root'

# f = flower(fruit)
# print(f())

print(root)
print('-----')
print(root())
print('-----')
root()

'''
# minimun number index position
arr = [15,16,27,13,8,32]
min = arr[0]
index_min = 0
for i in range(1, len(arr)):
    if arr[i] < min :
        min = arr[i]
        index_min = i
print(index_min)


class C(object):
    def __init__(self):
        self._x_ = 120
        self.x = 17
        self.x__ = 897
        self.__x__ = 76
        # self.__x = 23 #error

obj = C()
print(obj._x_)
print(obj.x)
print(obj.x__)
print(obj.__x__)'''
