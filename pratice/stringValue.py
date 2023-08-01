st = 'aaaabbbcczzzzzzyyy'
privous = st[0]
c = 1
i = 1
res = []
while i < len(st):
    if st[i] == privous:
        c += 1
    else:
        res.append(privous+str(c))
        privous = st[i]
        c = 1
    if i == len(st)-1: # for print last digit
        res.append(privous+str(c))
    i += 1

print(''.join(res))
# o/p = 'a4 b3 c2 z6 y3'


print('-----------------')

sy = 'a4k3b2'

reslt = ''

for i in sy:
    if i.isalpha():
        x = i
        reslt += x
    else:
        d = int(i)
        y = chr(ord(x)+d)
        reslt += y + ' '

print(reslt)
# o/p = 'aeknbd'

print('-----remove duplicate-----')


rm = 'gghffakjfjkfkafijifjifjasfjjkfdghshiuaiffshueuie'
li = []
strg =''
for i in rm:
    if i not in strg:
        strg += i
        li.append(i)
print(' '.join(strg)) #'g h f a k j i s u d e'
print(li) # 'ghfakjisude'
print(' '.join(set(rm))) # 's h a f k j g u d i e' -->unOrdered


print('---------count() occurance of each character-------')

cnt = 'gafgsdgsgf'
lit = []
for i in cnt:
    if i not in lit:
        lit.append(i)

for i in sorted(lit):
    print(f'{i} occurs {cnt.count(i)} times.')

print('______without using count_______')

s = 'abcbcaaassdffddgdddggb'
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1

for k,v in d.items():
    print('{1} times {0} occurs'.format(k,v))

print('---------------------')

s2 = 'abcbcaaassdffddgdddggb' # 5a 4b 3c 7d 3f 4g 3s
op = {}
res = ''
for i in s2:
    op[i] = d.get(i, 0)+ 1

for k,v in sorted(op.items()):
    res += str(v)+k+' '
print(res)

print('---------------------')

s3 = 'ABAABBCA' #A4B3C1
d = {}
result = ''
for i in s3:
    d[i] = d.get(i, 0) + 1

for k,v in sorted(d.items()):
    result += k+str(v)+' '
print(result)

print('-------vowel occurence count---------')

v = 'THESEARETHEVOWELMETHODyour impression is required.'
vowels = ['a', 'e', 'i', 'o', 'u']
d = {}
for i in v:
    if i or i.upper() in vowels:
        d[i] = d.get(i, 0) + 1

for k,v in sorted(d.items()):    
    print('Vowel - {} occurs {} times.'.format(k,v))


print('-----anagram-----') # (lazy or zaly and ylza or aylz)

v1 = 'listen' # 'triangle'
v2 = 'silent' # 'integral'
if sorted(v1) == sorted(v2):
    print('Both strings are Anagram')
else:
    print('Not Anagram')

print("_____palindrome_string______")

string = 'eavae'
x = string
r = ''
# for i in range(1,len(x)+1):
#     r =r + x[len(x)-i]
i = 1
while i <= len(x):
    r = r + x[len(x)-i]
    i += 1

if r == string:
    print('palindrome')
else:
    print('Not Palindrome')


# process 2

string2 = 'level'
if string2 == string2[::-1]:
    print('palindrome [::-1]')
else:
    print('Not Palindrome')

# process 3

string3 = 'malayalam'
rev = ''.join(reversed(string3))
if string3 == rev:
    print('palindrome reversed()')
else:
    print('Not Palindrome')

print('------------------------')

s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'
i=j=k=0
while i<len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i<len(s1):
        output += s1[i]
        i += 1
    if j<len(s2):
        output += s2[j]
        j += 1
    if k<len(s3):
        output += s3[k]
        k += 1
    print(output)