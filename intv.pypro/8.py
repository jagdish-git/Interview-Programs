data1 = ['1','2','3','4','5']
d=[3,0,2]


res = list(map(data1.__getitem__, d))
print(res)

li = []
for i in d: 
    li.append(data1[i])
print(li)

new = []
for i in data1:
    if data1.index(i) in d:
        new.append(i)
print(new)

