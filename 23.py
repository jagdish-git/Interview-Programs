# inputs = [0,1,8,1,2,4,2,3,3,2,0,2,7,0,5,0,2,1]

def sort_count(arr):
    dict1 = dict()
    for i in range(len(arr)):
        dict1[arr[i]] = dict1.get(arr[i], 0) + 1
    print(dict1)
    # sorted_dict = {k:v for k,v in sorted(dict1.items(), key= lambda c : c[1], reverse=True)}
    sorted_dict = dict(sorted(dict1.items(), key= lambda x:x[1], reverse=True))
    print(sorted_dict)
    final_list1 = []
    final_list2 = []
    for k,v in sorted_dict.items():
        if v <= 1:
            final_list1.append(k)
        else:
            for r in range(v):
                final_list2.append(k)
    print(final_list2+sorted(final_list1))

inputs = [0,1,8,1,2,4,2,3,3,2,0,2,7,0,5,0,2,1]
sort_count(inputs)