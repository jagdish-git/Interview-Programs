# Roman to Integer
# input : "III" output: 3 
# input : "LVIII" output: 58
# input : "MCMIV" output: 1904
romans = {
        "I": 1,"V": 5,"X": 10,"L": 50,
        "C": 100,"D": 500,"M": 1000
        }

# 1
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


def roman_to_int(strings):
    res = 0
    i = 0
    while i < len(strings):
        s1 = value(strings[i])
        if i+1 < len(strings):
            s2 = value(strings[i+1])
            if s1 >= s2:
                res = res + s1
                i = i + 1
            else:
                res = res + s2 -s1
                i = i + 2
        else:
            res += value(strings[i])
            i += 1
    return res


print(roman_to_int('LVIII'))


# 2

def romanToInt(strn):
    result = 0
    i = 0
    ln = len(strn)
    while i < ln:
        if i != ln-1 and romans[strn[i]] < romans[strn[i+1]]:
            result = result + romans[strn[i+1]] - romans[strn[i]]
            i += 2
            continue
        else:
            result += romans[strn[i]]
        i += 1
                       
    return result


print(romanToInt('MCMXCIV'))



def romanToInteger(s):
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        print(s)
        for char in s:
            number += romans[char]
            print(number)
        print(number)
         
romanToInteger('MCMXCIV')