# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Input: nums = [22,22,11,11,11,22,22]
# Output: 22

# Input: nums = [7,5,7]
# Output: 7

def majorityElement(nums):
    half = len(nums)//2
    for i in range(len(nums)):
        if nums.count(nums[i]) >= half:
            return nums[i]
    return 0
    

nums = [7,5,7, 8, 7, 11]
print(majorityElement(nums))

def majorityElement_dict(nums):
    dc = dict()
    for i in nums:
        dc[i] = dc.get(i,0)+1
    
    for k in dc.keys():
        if dc[k] >= len(nums)//2:
            return k
    return 0

nums = [22,22,11,11,11,22,22]
print(majorityElement_dict(nums))

def majorityElement_voting(nums):
    count = 0
    candidate = 0
    for n in nums:
        if count == 0:
            candidate = n
        if n == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate

nums = [6,7,6]
print(majorityElement_voting(nums))