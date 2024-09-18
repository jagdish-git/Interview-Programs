# while loop

def compress_while(st):
    prev = st[0]
    count = 1
    i = 1
    result = ''
    while i < len(st):
        if st[i] == prev:
            count += 1
        else:
            result += (prev + str(count))
            prev = st[i]
            count = 1
        if i == len(st)-1:
            result += (prev + str(count))
        i += 1    

    return result

s = 'aaaabbbbccc'
print(compress_while(s))



# for loop 


def compress_for(strn):
    size = len(strn)
    count = 1
    res = ''
    for i in range(size-1):
        if strn[i] == strn[i+1]:
            count += 1
        else:
            res += (strn[i] + str(count))
            count = 1
        # if i == size-2:
        #     res += (strn[i] + str(count))
    res = res + strn[size-1] + str(count)
    return res

string1 = 'abbcddeeeffggghhhh'
print(compress_for(string1))



# Another Problem

def uncompress(strn):
    result = ''
    for i in strn:
        if i.isalpha():
            x = i
            result += x
        else:
            d = int(i)
            y = chr(ord(x)+d)
            result += y 
    print(result)
string3 = 'a4k3b2'
uncompress(string3)
