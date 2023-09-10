# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    dct = {}
    for s in strs:
        srtd = ''.join(sorted(s))
        # if srtd not in dct:
        #     dct[srtd] = [s]
        # else:
        #     # dct[srtd] += [s]
        #     dct[srtd].append(s)
        dct[srtd] = dct.get(srtd, []) + [s]

    # res = []
    # for val in dct.values():
    #     res = [sorted(val)] + res
    # return res
    return sorted(list(sorted(v) for v in dct.values()), key= lambda x:len(x))


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))