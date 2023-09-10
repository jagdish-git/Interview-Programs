# remove dupliacte elements from the list
list1 = [4,5,1,3,2,1,4,3,1,2,5,4,6,3,1,2,7]

# Using set() method
def remove_duplicates_set(nums):
    return list(set(nums))

print(remove_duplicates_set(list1))


# Using list comprehension 
def rm_dup_lst_comp(nums):
    res = []
    [res.append(i) for i in nums if i not in res]
    return res

print(rm_dup_lst_comp(list1))

# Using list comprehension with enumerate()
def rm_dup_lst_comp_enumerate(nums):
    result = [n for index, n in enumerate(nums) if n not in nums[:index]]
    return result
print(rm_dup_lst_comp_enumerate(list1))

# using list comprehension and Array.index() method
def rm_dup_lst_comp_arr_index(nums):
    res = []
    for i in range(len(nums)):
        if i == nums.index(nums[i]):
            res.append(nums[i])

    return res

print(rm_dup_lst_comp_arr_index(list1))

# time O(n) , first sort then remove elements
def remove_dup_sort_list(nums):
    k = 0
    while k < len(nums)-1:
        if nums[k] > nums[k+1]:
            nums[k],nums[k+1] = nums[k+1], nums[k] #swap
            k = -1
        k = k+1
    # arr = sorted(nums)
    arr = nums
    i = 0
    while i < len(arr):
        if arr[i] == arr[i-1]:
            del arr[i] # arr.remove(arr[i])
            i = -1
        i = i + 1
    return arr
print(remove_dup_sort_list(list1))