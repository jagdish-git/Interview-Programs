dc = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# method 1 \

output_dict = dict(reversed(list(dc.items())))
print(output_dict)

# method 2 \

output_dict_2 = dict()
keys_dc = list(dc.keys())
for k in reversed(keys_dc):
    output_dict_2[k] = dc[k]
print(output_dict_2)

