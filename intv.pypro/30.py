list1 = [4,7,9,2,7,5,4,9,7,1,8,4,6,7,3,1,7]
# get the maximum repeated element
def max_ele(listx):
    m = 0
    li = []
    for x in listx:
        if x not in li:
            li.append(x)
    print(li)
    for i in li:
        if listx.count(i) > m :
            m = listx.count(i)
            result = i 
    return result

# print(max_ele(list1))

# use the dict method
def dict_max_ele(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i,0) + 1
    print(d)
    mx = 0
    for k in d.keys():
        if d[k] > mx:
            mx = d[k]
            res = k
    return res


d = dict_max_ele(list1)    
print(d)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for index, x in enumerate(fib()):
    if index == 10:
        break
    print("%s" % x, end=',')