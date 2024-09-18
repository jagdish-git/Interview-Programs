# Given an integer array nums, 
# return TRUE if any value appears at least twice in the array, 
# and return FALSE if every element is distinct.
# Input: nums = [1,2,3,1]
# Output: true
# Input: nums = [1,2,3,4]
# Output: false


# taking a list O(n) 
def containsDuplicate(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] in res:
            return True
        res.append(nums[i])
    return False

# hash map(dict) O(n)
def contains_dup_dict(nums):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and d[nums[i]] >= 1:
            return True
        d[nums[i]] = d.get(nums[i],0) +1
    return False

# sorting
def contains_dup_sort(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

# hash set 
def contains_dup_set(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False


# brute force
def conatins_dup_forloop(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return True
    return False




testcases=[
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
    [],
    ['x','y','x','p','z','p']
           ]

for nums in testcases:
    print(containsDuplicate(nums))

# for nums in testcases:
#     print(containsDuplicate(nums))

# for nums in testcases:
#     print(contains_dup_sort(nums))

# for nums in testcases:
#     print(contains_dup_set(nums))

# for nums in testcases:
#     print(conatins_dup_forloop(nums))