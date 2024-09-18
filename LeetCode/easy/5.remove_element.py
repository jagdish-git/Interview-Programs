# Remove Element
# nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]


class Solution:
    def removeElement(self, nums, val):
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count +=1
        return count, nums

s = Solution()
ans = s.removeElement([0,1,2,2,3,0,4,2], 2)
print(ans)