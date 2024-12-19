# could you find the longest non repeating string

def longest_unique_substring(string):
    longest_substring = ""
    seen = set()
    start = 0
    count_longest_substring = 0

    for end in range(len(string)):
        while string[end] in seen:
            seen.remove(string[start])
            start += 1
                
        count_longest_substring = max(count_longest_substring, (end-start) + 1)
        seen.add(string[end])
        current_substring = string[start:end + 1]
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring, count_longest_substring

strings =["abcabcdefghcde", "abcabcdbb", "bbbbbbb", "pwwkew"]
for string in strings:
    print(longest_unique_substring(string))


# Approach 2 - Unordered Map

def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    maxLength = 0
    charMap = {}
    left = 0
    
    for right in range(n):
        if s[right] not in charMap or charMap[s[right]] < left:
            charMap[s[right]] = right
            maxLength = max(maxLength, right - left + 1)
        else:
            left = charMap[s[right]] + 1
            charMap[s[right]] = right
    
    return maxLength

strings =["abcabcdefghcde", "abcabcdbb", "bbbbbbb", "pwwkew"]
for string in strings:
    print(lengthOfLongestSubstring(string))



# naive approach
def dict_longest_unique_substring(string: str) -> str:
    longest_substring = str()
    dict_str = dict()
    sub_str = str()
    count = 0
    maxx = 0
    for char in range(len(string)):
        if string[char] not in sub_str:
            sub_str += string[char]
            count += 1
        elif string[char] in sub_str:
            if count > maxx:
                longest_substring = sub_str
                maxx = count
            dict_str[sub_str] = count
            count = 1
            sub_str = string[char]
    dict_str[sub_str] = count
    # print(dict_str)

    return f"{longest_substring} has count of {maxx}"

# print(dict_longest_unique_substring('abcabcdefabcefabde'))
strings =["abcabcdefghcde", "abcabcdbb", "bbbbbbb", "pwwkew"]
for string in strings:
    print(dict_longest_unique_substring(string))