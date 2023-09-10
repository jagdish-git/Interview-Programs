# merge of two dictionary


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
print({**dict1},{**dict2})
print('Using  **kwargs : ',{**dict2,**dict1}) # **kwargs 
print('Using | OR : ',dict1 | dict2) # using | operator
dict1.update(dict2) # update() method
print('Using Update() : ',dict1)
