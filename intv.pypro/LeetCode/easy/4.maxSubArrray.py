# maximum subarray 

# 1 time : O(n2)
def max_sub_array(arr):
    lnarr = len(arr)
    maxSum = -1e8

    for i in range(lnarr):
        currSum = 0
        for j in range(i, lnarr):
            currSum = currSum + arr[j]
            if currSum > maxSum:
                maxSum = currSum
    return maxSum


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sub_array(arr))


# 2 time : O(n)
def maxSubArray(arr):
    n = len(arr)
    maxSum = -1e8
    currSum = 0
    
    for i in range(0,n):
        currSum = currSum + arr[i]
        if currSum > maxSum:
            maxSum = currSum
        if currSum < 0:
            currSum = 0

    return maxSum

if __name__ == "__main__":
    array = [5,4,-1,7,8]
    print(maxSubArray(array))