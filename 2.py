l1 = [1,2,3]
l2 = [4,5,6]
l3 = ['a','b','c']

x = dict(zip(l1,l2))
print(x)

new = []
for i in range(len(l1)):
    new.append(str(l1[i])+l3[i])
print(new)