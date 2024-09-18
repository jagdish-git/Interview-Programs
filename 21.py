# using For Loop by using temp(3rd var)

def sort_array(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

array = [4,7,9,13,3,6,15,11,2]
s = sort_array(array)
print(s)

# 2.
def sort_array_2(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    dup = []
    for i in arr:
        if i not in dup:
            dup.append(i)
    return dup

array2 = [7,4,9,13,3,6,15,11,2,15,13,6,7,2]
s2 = sort_array_2(array2)
print(s2)

# 3. sorted()
array3 = [22,33,11,4,16,13,15,7]
print(sorted(array3, reverse=True))

# 4.sort()
array4 = [22,33,11,4,16,13,15,7]
array4.sort(reverse=True)
print(array4)


# random list
def sort_2nd_ele(element):
    return element[1]

random = [(11, 2), (33, 4), (44, 1), (22, 3)]
print('--', sorted(random, key=sort_2nd_ele))
random.sort(key=sort_2nd_ele)
print(random)
