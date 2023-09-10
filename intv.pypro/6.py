list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['4', '5', '6']


print([str(i)+j for i,j in zip(list1,list2)])
print([''.join(x) for x in zip(list3,list2)])

for x,y in zip(list1,list2):
    print(str(x) + y, end=' ')

print()
for x in zip(list2, list3):
    print(''.join(x) ,end=' ')

new = []
for i in range(len(list1)):
    new += str(list1[i])+list2[i]
print(new)


def add_arr(l1, l2):
    news = []
    i = 0
    while i < len(l1):
        ln = len(str(l2[i]))
        news += [l1[i] * 10 ** ln + l2[i]]
        i += 1

    print(news)


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [4921, 57123, 6813]
add_arr(list1, list3)