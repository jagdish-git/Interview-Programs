data={'one':1,'three':3,'five':5,'two':2}


dict_comp = {key: value for key, value in sorted(data.items(), key=lambda i: i[1])}
tup= sorted(data.items(), key= lambda i: i[1])

print('In Dictionary comprehension', dict_comp) # {'one': 1, 'two': 2, 'three': 3, 'five': 5}
print('In List of Tuple Format', tup) # [('one', 1), ('two', 2), ('three', 3), ('five', 5)]

bykey = {k:v for k,v in sorted(data.items())}
print('Sort by key ',bykey) #{'five': 5, 'one': 1, 'three': 3, 'two': 2}

for i in sorted(data) :
    print ((i, data[i]), end =" ") #('five', 5) ('one', 1) ('three', 3) ('two', 2)

print('\n')
d = {}
t = {}
for k,v in data.items():
    t[v] = k
print(t) # {1: 'one', 3: 'three', 5: 'five', 2: 'two'}

for k in sorted(t.keys()):
    d[k] = t[k]

print(d) #{1: 'one', 2: 'two', 3: 'three', 5: 'five'}


