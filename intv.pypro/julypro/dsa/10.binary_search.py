from util import time_it


# binary search
@time_it
def linear_search(arr, number_find):
    for index, number in enumerate(arr):
        if number == number_find:
            return index
    return -1


@time_it
def binary_search(arr_list, number_to_search):
    left_index = 0
    right_index = len(arr_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = arr_list[mid_index]

        if mid_number == number_to_search:
            return mid_index

        if mid_number < number_to_search:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


def binary_search_recursive(number_list, number_to_finds, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(number_list) or mid_index < 0:
        return -1

    mid_number = number_list[mid_index]
    if number_to_finds == mid_number:
        return mid_index
    if mid_number < number_to_finds:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(number_list, number_to_finds, left_index, right_index)


if __name__ == "__main__":
    elements = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 50
    # elements = [i for i in range(1, 100001)]
    # number_to_find = 100000
    # print(linear_search(elements, number_to_find))
    # print(binary_search(elements, number_to_find))
    # print(binary_search_recursive(elements, number_to_find, 0, len(elements) - 1))


# exercise 1
#  When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
#  numbers = [1,4,6,9,10,5,7]
#  Answer: It is because the list is not sorted! Binary search requires that list has to be sorted

# exercise 2
# numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
# find the all occurrences of the sorted list
# number_to_find = 15   output = [5,6,7]

def find_occurrences(number_list, number_to_search):
    index = binary_search(number_list, number_to_search)
    indices = [index]
    print(index)
    # find indices on left hand side
    i = index - 1
    while i >= 0:
        if number_list[i] == number_to_search:
            indices += [i]
        else:
            break
        i = i - 1

    # find indices on left hand side
    i = index + 1
    while i <= len(number_list):
        if number_list[i] == number_to_search:
            indices += [i]
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == "__main__":
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15
    indices = find_occurrences(numbers, number_to_find)
    print(f"Indices of occurrences of {number_to_find} are {indices}")
