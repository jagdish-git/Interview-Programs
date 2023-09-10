# Combine the values of two dictionaries having same key


dict1 = {'nikhil': 1, 'akash' : 5,'manjeet' : 10, 'akshat' : 15}
dict2 = {'akash' : 7, 'akshat' : 5,'m' : 15}


#>>1
'''
from collections import Counter
print(Counter(dict1)) # Counter({'akshat': 15, 'manjeet': 10, 'akash': 5, 'nikhil': 1})
print(Counter(dict2)) #Counter({'m': 15, 'akash': 7, 'akshat': 5})
print(Counter(dict1) + Counter(dict2)) #Counter({'akshat': 20, 'm': 15, 'akash': 12, 'manjeet': 10, 'nikhil': 1})
'''

#>>2
print([k for k in set(dict2) & set(dict1)]) #['akash', 'akshat']
print([(k, dict1[k] + dict2[k]) for k in set(dict2) & set(dict1)]) # [('akash', 12), ('akshat', 20)]
print(dict([(k, dict1[k] + dict2[k]) for k in set(dict2) & set(dict1)])) # {'akash': 12, 'akshat': 20}


final1 = {k:(dict1.get(k,0) + dict2.get(k,0)) for k in dict1 | dict2}
final2 = {k:(dict1.get(k,0) + dict2.get(k,0)) for k in set(dict1) | set(dict2)}
final3 = {k:(dict1.get(k,0) + dict2.get(k,0)) for k in set(dict1).union(dict2)}

print(final1) #{'nikhil': 1, 'akash': 12, 'manjeet': 10, 'akshat': 20, 'm': 15}
print(final2) #{'manjeet': 10, 'm': 15, 'akshat': 20, 'nikhil': 1, 'akash': 12}
print(final3) #{'manjeet': 10, 'm': 15, 'akshat': 20, 'nikhil': 1, 'akash': 12}
