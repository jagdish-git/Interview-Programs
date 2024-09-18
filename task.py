input = """|Title1=COMING UP...|Catagory1=Line1|Title2=09:20|Catagory2=Line2|Title3=One Stop Science Shop|Catagory3=Line3|Title4=09:30|Catagory4=Line4|Title5=My Petsaurus|Catagory5=Line5|Title6=09:35|Catagory6=Line6|Title7=nil|Catagory7=Line7"""

output = "Line1=COMING UP...&Line2=09:20&Line3=One Stop Science Shop&Line4=09:30&Line5=My Petsaurus&Line6=09:35"

s = input.split("|")
title = dict()
category = dict()
for i in s:
    if i:
        if 'title' in i.lower():
            split_str = i.rpartition('=')
            title[split_str[0]] = split_str[-1]
            continue
        if 'catagory' in i.lower():
            split_str = i.rpartition('=')
            category[split_str[0]] = split_str[-1]
ls = list()
title_value = [i for i in title.values()]
category_value = [i for i in category.values()]
for i,j in zip(category_value, title_value):
    if j.startswith('nil'):
        break
    else:
        ls.append(i+"="+j)
print(ls)
string = "&".join(ls)
print(string)
print(string==output)

# # nx = mx.replace('|','&').replace('Title','Line').replace('Catagory','')
# # print(''.join(mx))
# # print(nx)
# # print(mx)
# # sp = mx.split('|')
# # for i in sp:
# #     print(i, end='__')
# # print(''.join(mx))




dict1 ={}
mx = input[1:]
sp = mx.split('|')
for i in sp:
    d = i.rpartition('=')
    dict1[d[0]] = d[-1]
# print(dict1)
# print()
new = ''
for x,y in dict1.items():
    if y.startswith('nil'):
        break
    if x.startswith('Title'):
        v = x.replace('Title', 'Line')
        new += f'{v}={y}'+'&'
    

print(new[:-1])
print(output)
print(new[:-1]==output)