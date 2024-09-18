# String Format
# 1. store in a string

def str_format(str1):
    split_str = str1.split('_')
    new_str = ''
    for i in split_str:
        new_str += i[:1].lower() + i[1:].upper() + '.'
    print(new_str) # I.Am.A.Coder.
    new_str = new_str[:-1]
    print(new_str) # I.Am.A.Coder

str1 = 'I_Am_A_Coder'
str_format(str1)

# 2. store in a list

def str_format(str1):
    split_str = str1.split('_')
    new_list = []
    for i in split_str:
        word = i[0].lower() + i[1:].upper()
        new_list.append(word)
    print('.'.join(new_list)) # tHIS.iS.a.tABLET

str1 = 'This_Is_A_Tablet'
str_format(str1)