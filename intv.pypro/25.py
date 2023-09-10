#1
def string(strx):
    str1 = strx.split()
    new_str = ''
    for i in range(len(str1)):
        if i != len(str1)-1:
            new_str =  '-' +str1[i] + new_str
        else:
            new_str = str1[i] + new_str
    print(new_str)

char = 'python is real'
string(char)

#2
def string2(strx):
    str1 = strx.split()
    new_str = ''
    for i in range(len(str1)):
        j = -(i+1)
        if i+1 != len(str1):
            new_str += str1[j] + ' '
        else:
            new_str += str1[j]
    print(new_str)
        
char = 'the sky is blue'
string2(char)