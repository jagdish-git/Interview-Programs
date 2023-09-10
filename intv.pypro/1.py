# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


nums = [2,7,11,15,19]
x = nums[0]
a = 26


for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]+nums[j] == a and i != j:
            print([i,j])
# output : [1,4] [2,3]
print('-------------')

v = []
for i in range(30):
    for j in range(i,30):
        if i != 0 and i != j and i + j == 30:
            v.append({i,j})

print(v) 

print('-------------')


eg = [1,2,3,4,5]

for i in range(len(eg)):
    for j in range(i, len(eg)):
        if eg[i] + eg[j] == 6:
            print([eg[i],eg[j]])
# output: [1,5] [2,4] [3,3]

print('------O(N)--------')
# Time complexity: O(N), Space Complexity: O(N);
# with one for loop


