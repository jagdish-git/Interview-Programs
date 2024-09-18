# # Dictionary Comprehension
# # { key:value for key,value in iterable}

keys = ['a','b','c','d','e']
values = [1,2,3,4,5]


# print({k:v for k,v in zip(keys,values)})
# print(dict(zip(keys,values)))

# print(dict.fromkeys(range(5,9), "keys"))

myDict = {n:n**3 for n in [3,4,5,6,7,8]}
# print(myDict)

strDict = {s.upper(): s*3 for s in 'python'}
# print(strDict)

newDict = {x:x**3 for x in range(10) if x**3 % 4 == 0}
# print(newDict)



# create a list comprehension with student age
data = [('sravan', 23), ('ojaswi', 15),
        ('rohith', 8), ('gnanesh', 4), ('bobby', 20)]

print({key: value for key,value in data})

print({key: value for (key, value) in data if value == 20})

print({key: value for (key, value) in data if value > 10})
 
print({key: value for (key, value) in data if key == 'sravan'})

