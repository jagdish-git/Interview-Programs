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
