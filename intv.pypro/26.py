# # Example:
# # Input: [a, b, c], [1, 2, 3]
# # Output: [a, 1, b, 2, c, 3]


# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3, 4]



# #1
# result = []
# for i,j in zip(list1,list2):
#     result =result + [i,j]
# print(result)

# # 2
# final = []
# for i in zip(list1,list2):
#     for j in i:
#         final.append(j)
# print(final)

# # 3
# final_list = [y for x in zip(list1,list2) for y in x] # list comprehension
# print('-----',final_list)
# #
# result2 = []
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if i == j:
#             result2.append(list1[i])
#             result2.append(list2[j])
# print(result2)


# add some extra values to a list
list3 = ['a', 'b', 'c']
list4 = [1, 2, 3, 4,5,6]

def concat(list_x,list_y):
    result = []
    len_x = len(list_x)
    len_y = len(list_y)
    # extra_value = list_x[len_y:] if len_x > len_y else list_y[len_x:]
    if len_x > len_y:
        extra_value = list_x[len_y:]
    else:
        extra_value = list_y[len_x:]
    # print([y for x in zip(list_x,list_y) for y in x] + extra_value)

    for i in range(min(len_x,len_y)):
        result += [list_x[i], list_y[i]]
        
    print(result.extend(extra_value))

concat(list3,list4)
    