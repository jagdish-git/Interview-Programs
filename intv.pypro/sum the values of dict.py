# Sum values for each key in nested dictionary

# 1. Find sum of sharpness values using sum() function

weapons = { '': None, 
            'sword': { 'steel': 151,'sharpness': 100,'age': 2,}, 
            'arrow': {'steel': 120,'sharpness': 205,'age': 1,}
           }

y=0
for k,val in weapons.items():
    if val and 'sharpness' in val.keys():
        y += val['sharpness']

print(y)

x = sum([v['sharpness'] for v in weapons.values() if v])
z = sum([v['steel'] for v in weapons.values() if v])
print(x)
print(z)

