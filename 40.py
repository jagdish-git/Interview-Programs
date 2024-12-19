# remove only first duplicate number in the list 

def find_first_duplicate(arr):
    new = set()
    empty = list()
    for index, num in enumerate(arr):
        if num in new: # if num in empty
            arr.pop(index)
            break
        new.add(num)
        # empty.append(num)

    return arr

lst = [5, 6, 3, 5, 7, 6, 1, 3, 6, 7]
print(find_first_duplicate(lst))


# another approach

def remove_first_duplicate(lst):
    unique_list = []
    
    for i in range(len(lst)):
        if lst[i] in unique_list:
            return lst[0:i] + lst[i+1:]
        else:
            unique_list.append(lst[i])
            
lst = [6, 8, 9, 5, 2, 3, 5, 8, 9, 1]
print(remove_first_duplicate(lst))
