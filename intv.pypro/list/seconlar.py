list1 = [10, 89,20, 4,45, 78,56,34,23,99]
 
mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and mx != list1[i]:
        secondmax=list1[i]

print("Second highest number is : ", str(secondmax))



largest = list1[0]
largest2 = None 
smallest = list1[0]
smallest2 = None
for item in list1[1:]:     
    if item > largest: 
        largest2 = largest
        largest = item 
    elif item > largest2 or largest2 == None : 
        largest2 = item
    if item < smallest: 
        smallest2 = smallest
        smallest = item 
    elif smallest2 == None or smallest2 > item: 
        smallest2 = item 

print(largest,largest2)
print(smallest,smallest)