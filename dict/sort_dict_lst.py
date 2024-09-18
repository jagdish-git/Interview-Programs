data = [    
    {'Name': 'Jake', 'Age': 40, 'Point': 20},
    {'Name': 'Sam', 'Age': 26},
    {'Name': 'Miller', 'Age': 20, 'Point': 50},
    {'Name': 'William', 'Age': 40, 'Point': 80},
    {'Name': 'Bob', 'Age': 29},
    {'Name': 'Charlie', 'Age': 30, 'Point': 70},
    {'Name': 'Kane', 'Age': 75},
    ]


# sorted(data)
# TypeError: '<' not supported between instances of 'dict' and 'dict'
from pprint import pprint

# pprint(sorted(data, key= lambda x: x['Age']))
# pprint(sorted(data, key= lambda x: x['Name']))
# pprint(sorted(data, key= lambda x: x['Age'], reverse=True))
# pprint(sorted(data, key= lambda n: (n['Age'], n['Name'])))


# pprint(sorted(data, key= lambda x: x.get('Age',100)))


# # sorted(data, key=lambda x: x['Point'])
# # KeyError: 'Point'

# sorted(data, key=lambda x: x.get('Point'))
# TypeError: '<' not supported between instances of 'int' and 'NoneType'

# pprint(sorted(data, key= lambda x: x.get('Point', 0)))
# pprint(sorted(data, key= lambda x: x.get('Point', 60)))
# pprint(sorted(data, key= lambda x: x.get('Point',float('inf'))))
## float('inf') represents towards a infinity value...
# pprint(sorted(data, key= lambda x: x.get('Point',float('-inf'))))


from operator import itemgetter

# pprint(sorted(data, key= itemgetter('Age'), reverse=True))
# pprint(sorted(data, key= itemgetter('Age')))
# pprint(sorted(data, key= itemgetter('Age', 'Name')))
# pprint(sorted(data, key= itemgetter('Point'))) ## keyerror


## get the minimum & maximum value
print(max(data, key=lambda i: i['Age']))
print(max(data, key=itemgetter('Name')))
print(max(data, key= lambda n: n.get('Age')))


print(min(data, key=lambda i: i['Age']))
print(min(data, key=itemgetter('Name')))
print(min(data, key= lambda n: n.get('Age')))
