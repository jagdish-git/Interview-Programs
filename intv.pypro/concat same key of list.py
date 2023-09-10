# Concatenate values with same keys in a list of dictionaries


#>>1

list1 = [{'gfg': [1, 5, 6, 7], 'good': [9, 6, 2, 10],'CS': [4, 5, 6]},
         {'gfg': [5, 6, 7, 8], 'CS': [5, 7, 10]},
         {'gfg': [7, 5], 'best': [5, 7]}]

e = {}
for dict in list1:
    for key in dict:
        print(key)
        if key in e:
            print('if---',dict[key])
            e[key] = e[key] + dict[key]
        else:
            print('else---',dict[key])
            e[key] = dict[key]

print(e)


#>>2
res = {}
for i in range(len(list1)):
    cur = list1[i]
    for k,v in cur.items():
        if k in res:
            res[k] = res[k] + cur[k]
        else:
            res[k] = cur[k]

print(res)


#Sum list of dictionaries with same key
ini_dict = [{'a':5, 'b':10, 'c':90},{'a':45, 'b':78},{'a':90, 'c':10}]
b = {}
for dic in ini_dict:
    for key in dic:
        if key in b:
            b[key] = b.get(key,0) + dic[key]
        else:
            b[key] = dic[key]

print(b)

sto = {}
for i in range(len(ini_dict)):
    dic = ini_dict[i]
    for key,val in dic.items():
        if key not in sto:
            sto[key] = dic[key]
        else:
            sto[key] += dic[key]
print(sto)


result = {}

for dict in ini_dict:
    for k in dict.keys():
        result[k] = result.get(k,0) + dict[k]
print(result)