# bubble sort
def bubble_sort(arr):
    for k in range(len(arr)-1):
        for i in range(len(arr)-1-k):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

list1 = [27,68, 43,2,19,37,6,15]
print(list1)
bbl = bubble_sort(list1)
print(bbl)


# bubble sort if the array already sorted
def bubble_flag_sort(arr):
    for k in range(len(arr)-1):
        flag = False
        for i in range(len(arr)-1-k):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
        if not flag:
            break
    return arr

list1 = [2, 4, 6, 15, 19, 27, 37, 43, 68]
# list1 = [34,35,36]
bbl = bubble_flag_sort(list1)
print(bbl)


# exercise on bubble sort

def bubble_sort_exr(elements, key='transaction_amount'):
    for i in range(len(elements)-1):
        swapped = False
        for j in range(len(elements)-1-i):
            x = elements[j][key]
            y = elements[j+1][key]
            if x > y:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
        if not swapped:
            break
    return elements

elements = [
    {'name':'mona', 'transaction_amount':1000, 'device':'iphone-10'},
    {'name':'dhaval', 'transaction_amount':400, 'device':'google pixel'},
    {'name':'kaithi', 'transaction_amount':200, 'device':'vivo'},
    {'name':'ajay', 'transaction_amount':800, 'device':'samsung'},
]
print(bubble_sort_exr(elements))