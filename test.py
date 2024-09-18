# balanced paranthesis
# input: "hello world"
# output: "d1r1w1o2l3e1h1"



def count_num_words(strs):
    dc = dict()
    for i in strs:
        if i != ' ':
            # dc[i] = dc.get(i,0) + 1
            if i in dc:
                dc[i] += 1
            else:
                dc[i] = 1

    
    print(dc)
    new = ''
    for k in dc.keys():
            new = k+str(dc[k]) + new
    print(new)

count_num_words("hello world")



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
    
    # Create the output string with counts
    output = ''.join(f"{char}{count}" for char, count in char_count.items())
    
    return output

# Test the function
input_string = "hello world"
output_string = count_characters_reversed(input_string)
print(output_string)



input_dict = {'h': 1, 'e': 1, 'r': 1, 'd': 1}
reverse_dict = {key:value for key,value in sorted(input_dict.items(), reverse=True)}
print(reverse_dict)

# Original dictionary
input_dict = {'h': 1, 'e': 1, 'r': 1, 'd': 1}

# Reverse the dictionary by sorting keys in descending order
reversed_dict = {k: input_dict[k] for k in sorted(input_dict, reverse=True)}


print(reversed_dict)
input_dict = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
mn = ''
ln = list(input_dict.keys())
for key in reversed(ln):
    mn += f"{key}{input_dict[key]}"


print(mn)



