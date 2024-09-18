# how to find the missing element in list or in a range
list1 = [0, 4, 6, 9, 8, 1, 3]

def find_missing(arr):
    for num in range(min(arr), max(arr)):
        if num not in arr:
            yield num

print(list(find_missing(list1)))