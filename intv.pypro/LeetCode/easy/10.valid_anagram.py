# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# here check Anagram or not
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false


# 1
def isAnagram(s,t):
    return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))

# 2
def isAnagram_dict(x,y):
    d = {}
    for i in x:
        d[i] = d.get(i,0)+1

    for j in y:
        d[j] = d.get(j,0)-1

    for k in d.keys():
        if d[k] != 0:
            return False
    return True

x = 'mission'
y = 'sominis'
print(isAnagram_dict(x,y))

# 3 Hash Table (Using Array)
def is_anagram_arr(a,b):
    count = [0]*26

    for i in a:
        count[ord(i) - ord('a')] += 1

    for j in b:
        count[ord(j) - ord('a')] -= 1
    
    for c in count:
        if c != 0:
            return False
    return True

a = "xyxx"
b = "xxxy"
print(is_anagram_arr(a,b))