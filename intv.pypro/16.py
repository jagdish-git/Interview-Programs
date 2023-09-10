# Character Occurance
# 1. Least occurance character using dict method

def least_char_dict(s):
    dict1 = {}
    for i in s:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1
    print(dict1)
    result = min(dict1, key=dict1.get)
    print(result)


string1 = 'abcdbcdaabbdab'
least_char_dict(string1)


#  2. counter builtin method

from collections import Counter
dict_counter = Counter(string1)
result = max(dict_counter, key=dict_counter.get)
print('collections.Counter -',result)

# 3. count method

count_str = string1.count('a')
print(count_str)


# get the particular char without count & with dict

def count_char_dict(s, search_ch):
    dict1 = {}
    for i in s:
        dict1[i] = dict1.get(i,0) + 1
    print(dict1)
    try:
        print(dict1[search_ch])
    except:
        print(f'{search_ch} not found')

string2 = 'zyxzyzyxyzyxy'
char1 = 'b'
count_char_dict(string2,char1)