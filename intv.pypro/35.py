input_list = ['1','1.3','1.14','1.11']
op = ['1', '1.3', '1.11', '1.14']

output = sorted(input_list, key=lambda x: (len(x),x))
print(output)
print(output==op)


def sort_list_dict(listx):
    listx.sort()
    dictt = {i:len(i) for i in listx}
    sort_dict = {k:v for k,v in sorted(dictt.items(), key=lambda n:n[1])}

    result = [k for k in sort_dict.keys()]

    return result

testcases = [['1','1.3','1.14','1.11'],
             ['1.09','1.3','1.111','1.14','1.010','1.11','1.01'],
             [],
             ['0.2332','0.01','0.2','0', '0.00']
            ]
for listx in testcases:
     print(sort_list_dict(listx))


def sort_list(list1):
    for i in range(len(list1)):
        for j in range(0, len(list1)-i-1):
            if len(list1[j]) > len(list1[j+1]):
                    list1[j],list1[j+1] = list1[j+1],list1[j]
            elif len(list1[j]) == len(list1[j+1]):
                 if float(list1[j]) > float(list1[j+1]):
                      list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1

testcases = [['1','1.3','1.14','1.11'],
             ['1.09','1.3','1.111','1.14','1.010','1.11','1.01'],
             [],
             ['0.2332','0.01','0.2','0', '0.00']
            ]
# for listx in testcases:
#      print(sort_list(listx))
