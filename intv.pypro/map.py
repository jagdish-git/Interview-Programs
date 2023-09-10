# map(function, iteration)
# 1. with defined fun
def addition(n):
    return n+n
x = map(addition, [2,3,4])
print(list(x))

# lambda
nums = [4,5,6,7,8]
l = set(map(lambda x:x**2, nums))
print(l)

# add 2 list using lamda & map
l1 = [3,4,5]
l2 = [2,1,0]
print(tuple(map(lambda x,y,z:x+y+z, l1,l2, [5,5,5])))


# List of strings
lis = ['sat', 'bat', 'cat', 'mat']
print(set(map(tuple, lis)))
