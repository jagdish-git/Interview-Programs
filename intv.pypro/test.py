lkey = ['a','b','c']
tkey = (1,3,5,6)
d = {}
d[str(lkey)] = 345
d[tkey] = 678
for k,v in d.items():
    print(k,'-',v)