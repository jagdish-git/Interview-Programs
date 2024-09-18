# Two Sum Leetcode:1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9


# time complexity: O(n)
def twoSum(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        if target - nums[i] in num_dict:
            return [num_dict[target-nums[i]], i]
        num_dict[nums[i]] = i
    return []


if __name__ == "__main__":
    testcases = [2,7,11,15]
    target = 9
    print(twoSum(testcases, target))


# using two pointers method
# time O(n) and space o(1)
def two_sum_two_pointers(arr, target):
    i,j = 0, len(arr)-1
    while i < j:
        res = arr[i]+arr[j]
        if res == target:
            yield (i, j)
        elif res < target:
            i += 1
        else:
            j -= 1
    return []

list1 = [3,6,9,12,15,17]
print(two_sum_two_pointers(list1, 15))
      

# brute force method/ sorting method O(n2)
def two_sum_forloop(list1, target):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] + list1[j] == target:
                return [i,j]

if __name__ == "__main__":
    testcases = [2,7,11,15]
    target = 9
    print(two_sum_forloop(testcases, target))