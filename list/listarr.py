arr = [66,44,11,77,55,99,88,33,22]

# find the largest element from the array
print(max(arr))
print(sorted(arr)[-1])
#...
maxx = arr[0]
for element in arr: # range(len(arr))
    if element > maxx: # arr[element]
        maxx = element # maxx = arr[element]
print(maxx)

print(arr)
# find the smallest element from the array
print(min(arr))
print(sorted(arr)[0])
#...
minn = arr[0]
for num in range(len(arr)):
    if arr[num] < minn :
        minn = arr[num]
print(minn)


# Input : [81, 52, 45, 10, 3, 2, 96] 
#         N = 3
# Output : [81, 96, 52]

inp = [81, 52, 45, 10, 3, 2, 96] 

def Nmaxelement(lst, n):
    empty_list = []
    for _ in range(n):
        maxx = 0 # maxx=lst[0]
        for element in lst:
            if element > maxx:
                maxx = element
        lst.remove(maxx)
        empty_list.append(maxx)
    return empty_list, maxx

nmax = Nmaxelement(inp, 3)
print(nmax)    # [96, 81, 52]