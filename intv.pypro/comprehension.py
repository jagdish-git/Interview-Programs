#1 List Comprehension
list1 = [nums for nums in range(20) if nums%2 != 0]
print(list1)

list2 = [j for i in zip(list1[:5], list1[5:]) for j in i]
print(list2)


#2 dict comprehension
dict1 = {k:v for k,v in zip(list1[:5], list1[5:])}
print(dict1)


#3 set comprehension
import random
arr = [random.randint(2,17) for _ in range(29)]
print(arr)
set1 = {arr[s] for s in range(len(arr)) if arr[s]%2 != 0}
print(set1)


#4 generator comprehension
gen = (i for i in range(22) if i > 1 and i%2 == 0)
print(tuple(gen))
