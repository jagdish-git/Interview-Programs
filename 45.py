import re

# Reverse the character only
string = "!!j@@a###g$$d**i&&s**h"
# output = "!!h@@s###i$$d**g&&a**j"

# approach 1 (list)
def reverse_only_character(string):
    letters = [letter for letter in string if letter.isalpha()]
    total_string = []
    for char in string:
        if char.isalpha():
            total_string.append(letters.pop())
        else:
            total_string.append(char)
             
    return "".join(total_string)

print(reverse_only_character(string))

# approach 2 (two pointer)
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

print(reverse_only_character_two_pointer(string))