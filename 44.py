import re

#  Reverse the "jagdish" only on the above string
string = "$@&*%&jagdish#@$bal@&kbc@$9876#@"
output = "$@&*%&hsidgaj#@$bal@&ckb"


def find_reverse_name(string):
    result = ''
    result_num = ''
    total_str = ''
    for i in string:
        if i.isalpha():
            result += i
        # elif i.isnumeric():
        #     result_num += i
        else:
            if result:
                total_str += result[::-1]
                result = ""
            # if result_num:
            #     total_str += result_num[::-1]
            #     result_num = ""
            total_str += i
    if result:
        total_str += result[::-1]
    # if result_num:
    #     total_str += result_num[::-1]

    return total_str

print(find_reverse_name(string))

def find_rev_all_substring_regex(string):

    result = re.sub(r'[a-zA-Z0-9]+', lambda match: match.group()[::-1], string)
    print(result)
    pass

find_rev_all_substring_regex(string)




# simple type
string_simple = "$@&*%&jagdish#@$@&"
# output = "$@&*%&hsidgaj#@$@&"
#approach 1 (index postion)
def find_string_index_postion(string):
    start_index = string.index("jagdish")
    end_index = start_index + len("jagdish")

    reversed_substring = string[start_index:end_index][::-1]

    result = string[:start_index] + reversed_substring + string[end_index:]

    return result 

print(find_string_index_postion(string_simple))


# approach 2 (regex module)
import re

string_re = "$@&*%&jagdish#@$@&"

output_re = re.sub(r'jagdish', lambda x: x.group()[::-1], string_re)

print(output_re)

# approach 3 (spliting)
string_split = "$@&*%&jagdish#@$@&"
substring = "jagdish"

# Split the string and rejoin with the reversed substring
output_split = string_split.replace(substring, substring[::-1])

print(output_split)

