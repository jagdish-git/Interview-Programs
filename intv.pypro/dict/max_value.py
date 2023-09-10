cars = {'Audi': 5000, 'Rover': 4000, 'BMW':9999, 'Tesla':7000, 'Jaguar':6500}

#1 max-ZIP inbuilt method
def dict_max_value(dictz):
    zipv = zip(dictz.values(), dictz.keys()) #[(5000, 'Audi'), (4000, 'Rover'), (9999, 'BMW'), (7000, 'Benz'), (6500, 'Jaguar')]
    zipk = zip(dictz.keys(), dictz.values()) #[('Audi', 5000), ('Rover', 4000), ('BMW', 9999), ('Benz', 7000), ('Jaguar', 6500)]
    result_values = max(zipv)[0]
    result_keys = max(zipk)[0]
    print('Keys:', result_keys)
    return f'Max_Value: {result_values}'

d = dict_max_value(cars)
print(d)

#2 max_KEY params method 
def max_value_key(dictx):
    another =  max(dictx, key= lambda x : dictx[x])
    print(another) 
    res = max(dictx.items(), key= lambda i:i[1])[0]
    return res 
m = max_value_key(cars)
print(m)


#3 \\

def max_dict_value_list(dictv):
    k = list(dictv.keys())
    v = list(dictv.values())
    print(k, v)
    result = k[v.index(max(v))]
    print(result)

max_dict_value_list(cars)

# 4 \\
import operator
result = max(cars, key=operator.itemgetter(1))[0]
print('collections.Counter -',result)