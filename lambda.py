# lambda arguments: expression
# 1.11
x ='GeeksforGeeks'
(lambda x : print(x))(x)

# 1.12
tables = [lambda x=x: x*10 for x in range(1, 11)]
for t in tables:
    print(t(), end=' ')
print()
# 1.13
Maxy = lambda a, b : a if(a > b) else b
print(Maxy(11,22))

# 1.14
list1 = [23, 45, 21, 17, 19, 10, 14]
print(list(filter(lambda x:x>18 , list1)))

# 1.15
map_list = ['xyz','abc', 'efg', 'pqr','mno', 'ijk']
print(list(map(lambda x:str.upper(x), map_list)))

map_list2 = [22,55,66,77,88]
print(list(map(lambda x:x//11, map_list2)))


# 2
arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
print(list(filter(lambda x: x in arr1,arr2)))