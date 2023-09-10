# sort the array O(n) - one loop, without any inbuilt function

inputz = [11,-41,29,-13,58,9,-72]
input2 = [17, -35, 30, -74, -10, 4]

#1 while loop
def sort_one_while_loop(arr):
    length = len(arr)
    j = 0
    while j < length-1:
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j = - 1
        j = j + 1
    return arr

s = sort_one_while_loop(inputz)
print('Using While Loop :',s)


#2 using for loop
def sort_single_for_loop(arr):
    length = len(arr) # if length = 6
    for i in range(length**2): # iteration will 36 times
        i = i % length
        if i != length-1 and arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr

f = sort_single_for_loop(inputz)
print('Using For Loop   :', f)



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


string = 'THIS IS MY FIRST DATE having'
join_str = ''.join(string.split()) # THISISMYFIRSTDATE
list_str = [join_str[i] for i in range(len(join_str))]
# ['T', 'H', 'I', 'S', 'I', 'S', 'M', 'Y', 'F', 'I', 'R', 'S', 'T', 'D', 'A', 'T', 'E']
array_join = [0]*len(join_str)
for i in range(len(join_str)):
    array_join[i] = join_str[i]


#3 sort the string 
def sort_str_one_loop(strx):
    length = len(strx)
    j = 0
    while j < length -1 :
        if strx[j] > strx[j+1] :
            strx[j],strx[j+1] = strx[j+1],strx[j]
            j = -1
        j = j + 1
    return ' '.join(strx)

x = sort_str_one_loop(array_join)
print(x)


#4 sort the string for loop
def sort_str_for_loop(strz):
    txt = ''.join(strz.split())
    word = list(txt)
    print(sorted(word))
    for i in range(len(word)**2):
        i = i % len(word)
        if i != len(word)-1 and word[i] > word[i+1]:
            temp = word[i]
            word[i] = word[i+1]
            word[i+1] = temp
    print(''.join(word))

sort_str_for_loop(string)



#TypeError: 'str' object does not support item assignment
# String can't be swapped directly.
# you have to 1st convert into list. then you could swap the string