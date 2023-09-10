arr= ["a", "b", "c","d","a","e","f","b","a"]

d = {}
for i in arr:
    d[i] = d.get(i,0) + 1

# print(d)


Input_Array = {0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1}
Expected_Output = {1,1,1,1,1,1,2,2,2,2,6,6,0,0,3,5,8,9}

arr = [0,1,8,1,7,1,9,1,2,2,6,2,6,0,1,2,3,5,1]
dict1 = {}
for i in arr:
    dict1[i] = dict1.get(i,0) + 1
print('dict_format', dict1, '\n')
sort_dict = {k:v for k,v in sorted(dict1.items(), key=lambda x:x[1])[::-1]}
print('sort_dict', sort_dict, '\n')
list1,list2 = [],[]

for k in sort_dict.keys():
    if sort_dict[k] <= 1:
        list2.append(k)
    else:
        for v in range(sort_dict[k]):
            list1.append(k)
print('Output_Array ', list1+sorted(list2))
