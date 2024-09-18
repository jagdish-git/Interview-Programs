# merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left_arr = merge_sort(left)
    right_arr= merge_sort(right)

    return merge_two_sorted_list(left_arr, right_arr)

def merge_two_sorted_list(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i =i+1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i =i+1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list



if __name__ == '__main__':
    arr = [21, 38, 29, 17, 4, 25, 32, 9]
    # a = [5,8,9,11, 44, 55, 66]
    # b = [4,7,10,18]
    print(merge_sort(arr))


# merge sort without take a new list

def merge_sort2(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort2(left)
    merge_sort2(right)

    merge_two_sorted_list2(left, right, arr)

def merge_two_sorted_list2(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
    
    
if __name__ == '__main__':
    new_arr = [10,3,15,7,8,23,98,29]
    merge_sort2(new_arr)
    print(new_arr)