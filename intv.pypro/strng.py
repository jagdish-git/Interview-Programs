char = 'python is real'
sp = char.split()
print(char,len(char),sp[len(sp)-1])
sto = ''
for i in range(len(sp)):
    if i != len(sp)-1:
        sto = ' ' + sp[i] + sto
    else:
        sto = sp[i] + sto

print(sto, len(sto))


char2 = 'python is real'
spx = char2.split()
stor = ''
for i in range(len(spx)):
    j = -(i+1)
    if i+1 != len(spx):
        stor += spx[j] + '-'
    else:
        stor += spx[j]

print(stor)


# reverse the charcters of a word in a sentence

char3 = 'python is real'

def change(char):
    splt =  char.split()
    result = ''
    for ch in range(len(splt)):
        rev = ''
        for i in splt[ch]:
            rev = i+rev
        if ch != len(splt)-1 :
            result = ' ' + rev + result
        else:
            result = rev + result

    return result

print(change(char3))


# slicing method

def remove_last_space(str1):
    split_str = str1.split()
    new_str = ''
    for i in split_str:
        new_str = i +'-'+ new_str
    print(new_str)
    new_str2 = new_str[:-1]
    print(new_str2)


str1 = 'Apples Are Teasty'
remove_last_space(str1)