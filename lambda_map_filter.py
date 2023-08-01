y = [3,4,5,6,7,8]
lamb1 = list(map(lambda x: x*2, y))
lamb2  = list(filter(lambda x:x%2==0, y))
print(lamb1)
print(lamb2)

def square(n):
    return n*n
map_ = list(map(square, y))
print(map_)

def square(n):
    return n%2 != 0
filter_ = list(filter(square, y))
print(filter_)
