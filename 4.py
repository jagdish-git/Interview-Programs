dict1 = {"month":"January","days":31}
dict2 = {"month":"March","days":31}

for k in dict1:
    if dict1[k] in dict2.values():
        print({k: dict1[k]})

dc = {key:dict1[key] for key in dict1 if key in dict2 and dict1[key]==dict2[key]}
print(dc)