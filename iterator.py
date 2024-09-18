listx = ['W', 33, False, 45.98, 'String']
itr = iter(listx)

itr2 = listx.__iter__()
print(tuple(itr2))
print(type(itr))
print(next(itr))
print(next(itr))
print(itr.__next__())
print(itr.__next__())
print(next(itr)) # listx end here
# print(next(itr))  this will give : StopIteration
