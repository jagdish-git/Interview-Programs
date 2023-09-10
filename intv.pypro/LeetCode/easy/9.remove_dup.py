# Remove Duplicates from Sorted Array
# nums = [0,0,1,1,1,2,2,3,3,4]
# output = 5

def removeDuplicates(arr):
    count = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            nums[count] = arr[i]
            count += 1
    return count

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
    print(nums)