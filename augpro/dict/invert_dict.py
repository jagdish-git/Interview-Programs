# dict invert

def dict_invert(dc):
    new_kv = {}
    for k,v in dc.items():
        new_kv[v] = k
    print(new_kv)

    new_k= {}
    for key in dc.keys():
        # new_k[dc[key]] = key
        new_k[dc.get(key)] = key
    print(new_k)

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(dict_invert(original_dict))

# method 1
output_dict = {v:k for k,v in original_dict.items()}
output_dict_2 = {original_dict[k]: k for k in original_dict.keys()}
output_dict_3 = dict((v,k) for k,v in original_dict.items())
# print(output_dict)
# print(output_dict_2)
# print(output_dict_3)
map_dict = {'xxx': 40, 'kkk': 60, 'ddd': 80}
map_output_dict = dict(map(reversed, map_dict.items()))
print(map_output_dict)
# zip and lambda

invert = lambda mydict: {v:k for k,v in mydict.items()}
# print('.........', invert(map_dict))

invert_zip = lambda mydict: dict(zip(mydict.values(), mydict.keys()))
# print(',,,,,,', invert_zip(map_dict))


# method 2 (duplicate key)
# dict doesn't contain any duplicate key

def inverse_dict(dictc):
    res = {}
    for k, v in dictc.items():
        # res[v] = res.get(v, []) + [k]
        if v in res:
            res[v].append(k)
        else:
            res[v] = [k]
    return res

d = dict(a=1, b=2, c=1, d=3, e=2, f=1, g=5, h=2)
print(inverse_dict(d))

# method 3 (setdefault)
class ReversableDict(dict):
    def reverse_dict(self):
        revdict = {}
        for k, v in self.items():
            revdict.setdefault(v, []).append(k)
        return revdict

ex ={'a': 3, 'c': 2, 'b': 2, 'e': 3, 'd': 1, 'f': 2}
rv = ReversableDict(ex)
print(rv.reverse_dict())


# method 4 dict comprehension (multiple values)
dictc ={'a': 3, 'c': 2, 'b': 2, 'e': 3, 'd': 1, 'f': 2}
res = {v: [k for k in dictc if dictc[k] == v] for v in dictc.values()}
# res2 = {v:[i for i in d.keys() if d[i] == v ] for k,v in d.items()}
print(res)

# unpack the multiple dict values
some_dict = {1:{"a","b","c"},
        2:{"d","e","f"},
        3:{"g","h","i"}}

result_dict = {val:key for key,value in some_dict.items() for val in value}
print(result_dict)

# collection and defaultdict

from collections import Counter, defaultdict

def invert_dict(d):
    d_inv = defaultdict(list)
    for k, v in d.items():
        d_inv[v].append(k)
    return d_inv

text = 'aaa bbb ccc ddd aaa bbb ccc aaa' 
c = Counter(text.split()) # Counter({'aaa': 3, 'bbb': 2, 'ccc': 2, 'ddd': 1})
print(dict(invert_dict(c))) # {1: ['ddd'], 2: ['bbb', 'ccc'], 3: ['aaa']}  