## Sort a Dictionary by Value in Python
import operator
my_dict = {'a': 2, 'b': 1, 'c': 3}
sort_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
# print(sort_dict)

## dict of dictionary using lambda soreted method

data = {'Billy Sher': 30, 'Jane Doe': 25, 'Bill Smith': 40}

sored_dict_dict = sorted(data.items(), key= lambda x:x[1])
# result_dict = dict(sored_dict_dict)
result_dict = [{k:v} for k,v in sored_dict_dict]

# print(result_dict)

## list of dictionary using lambda soreted method
## sorted method return only as a LIST[]

data = [
    {'Billy Sher': 30}, {'Jane Doe': 25}, {'Bill Smith': 40},
    {'Gunshar Hemlet': 55}, {'Xavier Dane': 10}, {'Daniel Ken': 70} 
    ]

def sort_by_key(dicts):
    return list(dicts.keys())

def sort_by_value(dicts):
    return list(dicts.values())

sored_dict_list = sorted(data, key= sort_by_value)


## sored_dict_list = sorted(data, key= lambda x: list(x.values())[0])

# print(sored_dict_list)


## tuple of dictionary using lambda soreted method

data = (
    {'Billy Sher': 30}, {'Jane Doe': 25}, {'Bill Smith': 40}
    )

sored_dict_tup = tuple(sorted(data, key= lambda x: list(x.values())[0]))

# print(sored_dict_tup)



## using bubble sort method for sorting the dict by values

def sort_dict_bubble(data):
    
    for i in range(len(data)-1):
        for j in range(0,len(data)-1-i):
            if list(data[j].values())[0] > list(data[j+1].values())[0]:
                data[j], data[j+1]= data[j+1], data[j]
            
    return data


data2 = [
    {'Billy Sher': 30}, {'Jane Doe': 25}, {'Bill Smith': 40},
    {'Gunshar Hemlet': 55}, {'Xavier Dane': 10}, {'Daniel Ken': 70} 
    ]

print(sort_dict_bubble(data2))