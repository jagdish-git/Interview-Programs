input = 'abcdefghijkl'

# remove the n number index from the above string
# method - 1 (inbuilt)
n = 5
print(input.replace(input[n-1], '*'))

# method - 2 (slicing)
print(input[:n-1]+"#"+input[n:])


# method - 3 (naive)
def replace_chr(string, n):
    new_str = ''
    for i in range(len(string)):
        if i == n-1:
            new_str += "@"
        else:
            new_str += string[i]
    return new_str

print(replace_chr(input, 5))

# method  - 4 (list)
def list_replace_string(strings, target, val):
    list_str = list(strings)
    list_str[target-1] = val
    return ''.join(list_str)

print(list_replace_string(input, 5, "^"))

# method -5 (regex)
import re
print(re.sub(input[n-1], "!", input))

# Replace Multiple character with the same character
def replace_string_multiple_index(strings, target, val):
    for x in target:
        strings = strings[:x-1] + val + strings[x:] 
    return strings

print(replace_string_multiple_index(input, [2, 6, 8], "-"))

# Replace Multiple character with the different character
def replace_string_multiple_index_char(strings, targets):
    for key,val in targets.items():
        strings = strings[:key-1] + targets[key] + strings[key:] 
    return strings

indexs = {2:'~', 6:'&', 8:'%'}
print(replace_string_multiple_index_char(input, indexs))
