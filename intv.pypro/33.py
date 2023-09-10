# check the list is sorted or not
# def check_if_sorted(arr):
#     i = 0
#     while i < len(arr)-1:
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             i = -1
#         i += 1
#     return arr

# print(check_if_sorted([9,3,7,1,8,2,5]))

# 1. Naive Approach :  merge two sorted list
def merge_two_sorted_list(list1, list2):
    merge_list = []
    i = j = 0
    # sort_list1 = check_if_sorted(list1)
    # sort_list2 = check_if_sorted(list2)
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1
    # merge_list.extend(list1[i:])
    # merge_list.extend(list2[j:])
    while i < len(list1):
        merge_list.append(list1[i])
        i += 1
    while j < len(list2):
        merge_list.append(list2[j])
        j += 1

    return merge_list

list1 = [1, 3, 20, 12, 11]
list2 = [2, 34, 16, 8]
print(merge_two_sorted_list(list1, list2))


# 2 Using itertools.chain() and sorted()
import itertools
lst1 = [1, 5, 6, 9, 11]
lst2 = [3, 4, 7, 8, 10]

print(list(sorted(itertools.chain(lst1,lst2))))

# merge without taking a variable
def merge_sorted_list_without_new_variable(list1, list2):
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        else:
            list1.insert(i, list2[j])
            i += 1
            j += 1
    # list1.extend(list2[j:])
    while j < len(list2):
        list1.append(list2[j])
        j += 1
    
    return list1    
    
print(merge_sorted_list_without_new_variable(lst1,lst2))