# input: "hello world"
# output: "d1r1w1o2l3e1h1"


def count_alphabets(strn):
    dicts = {}
    new = ''
    for char in strn:
        if char not in ' ':
            dicts[char] = dicts.get(char, 0) + 1
    print(dicts)
    # output = ''.join(f"{char}{count}" for char, count in dicts.items())
    # print(output)
    for k in dicts.keys():
        new = k+str(dicts[k]) + new
    
    return new


inpt = "hello world"
print(count_alphabets(inpt))



# 2

def count_num_words(strs):
    dc = dict()
    for i in strs:
        if i != ' ':
            # dc[i] = dc.get(i,0) + 1
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1

    # print(dc)
    new_str = ''
    # reverse the dict
    rev_dict = dict(reversed(list(dc.items())))
    print(rev_dict)
    for k in rev_dict.keys():
            new_str += k+str(rev_dict[k])
    print(new_str)

count_num_words("hello world")


# 3

def count_characters_reversed(input_string):
    # Reverse the input string
    reversed_string = input_string[::-1]
    
    # Dictionary to store the count of each character
    char_count = {}
    
    # Count occurrences of each character
    for char in reversed_string:
        if char != ' ':  # Skip spaces
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    # Create the output string by iterating through the dictionary
    output = ''
    for char in reversed_string:
        if char != ' ' and char in char_count:
            output += f"{char}{char_count[char]}"
            del char_count[char]  # Remove the character after processing
    
    return output

# Test the function
input_string = "hello world"
output_string = count_characters_reversed(input_string)
output_string




# reverse the dictionary

input_dict = {'h': 1, 'e': 1, 'r': 1, 'd': 1}

# method builtin :
output_dict_l = dict(reversed(list(input_dict.items())))
print(output_dict_l)

# method another:
output_dict = {}

# Convert dictionary to a list of keys to process in reverse order
keys = list(input_dict.keys())

# Iterate over the keys in reverse order and add to the output dictionary
for key in reversed(keys):
    output_dict[key] = input_dict[key]

print(output_dict)