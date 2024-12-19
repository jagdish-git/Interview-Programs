string = "dlrow-olleh"

def reverse_only_character_two_pointer(string):
    s = list(string)
    left, right = 0, len(s)-1
    while left < right:
        if not s[left].isalpha():
            left += 1
        elif not s[right].isalpha():
            right -= 1
        else:
            # Swap the characters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    return ''.join(s)

# print(reverse_only_character_two_pointer(string))



def two_pointer_reverse(string):
    string = list(string)
    left =  0
    right = len(string)-1
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    
    return ''.join(string)

# print(two_pointer_reverse(string))


# in the below approach, think like a graph draw
def find_peak(array):
    peaks = list()
    for num in range(len(array)-1):
        if array[num] > array[num-1] and array[num] > array[num+1]:
            peaks.append({num:array[num]})

    one_line = [{n:array[n]} for n in range(len(array)) if array[n] > array[n-1] and array[n] > array[n+1]] 
    return peaks, one_line
    

array = [-1, 0, 1, 2, 1, 0, -1, -2, -1, 0, 2, 3, 1, -1, 0, 1, 2, 1, 0, -1, -2]
print((find_peak(array)))