def convert(input):
    new_dict = {}
    for i,j in input.items():
        if type(j) == dict:
            for k,l in j.items():
                new_dict.update({'_'.join(i+k):l})
        else:
            new_dict.update({i:j})
    return new_dict

input = {'a': 1, 'b': 2, 'c': {'d': 5, 'e': 6}}
c = convert(input)
print(c)

# output = {'a':1,'b':2,'c_d':5,'c_e':6}

#without use of function
'''
new_dict = {}
for i,j in input.items():
    if type(j) == dict:
        for k,l in j.items():
            new_dict.update({'_'.join(i+k):l})
    else:
        new_dict.update({i:j})

print(new_dict)
'''