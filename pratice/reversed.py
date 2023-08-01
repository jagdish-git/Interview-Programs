text = 'hello world'
s = text[::-1]
print(s)
r = reversed(text)
print(''.join(r))

text2 = 'Use While Loop'
print(len(text2))
res = ''
len_ = len(text2)-1
print(len_)
while len_>=0:
    res = res + text2[len_]
    len_ = len_ - 1
print(res)
    

text3 = 'welcome to world'
store = ''
len_2 = len(text3)
for i in range(1,len_2+1):
    store = store + text3[len_2-i]
print(store)


text4 = 'Python is easy for reading and writing'
print(text4.split()[::-1])
c = reversed(text4.split())
print(' '.join(c))
split_text4 = text4.split()
a = ''
for i in range(1,len(split_text4)+1):
    a  = a + split_text4[len(split_text4)-i] + ' '
print(a)


text5 = 'Hello World , This is New'
sp = text5.split()
strg = []
for i in sp:
    strg.append(i[::-1])

print(' '.join(strg))



text6 = 'one two three four five six seven'
spl = text6.split()
v = []
for i in range(len(spl)):
    if i%2==0:
        v.append(spl[i])
    else:
        v.append(spl[i][::-1])
print(' '.join(v))


print('------------========')

# even , odd index using while loop

text7 = 'abcdefghijklmnopqrsuvwxyz'
print(text7[0::2])
print(text7[1::2])

print('odd characters:')

i = 0
while i < len(text7):
    print(text7[i] ,end=' ')
    i += 2

print()
j = 1
print('even characters:')
while j < len(text7):
    print(text7[j], end=' ')
    j += 2

print('\n-----------------')
x ='B4A1D3'
ch = []
num = []
ch2 = ''
num2 = ''
for i in x:
    if i.isalpha():
        ch.append(i)
        ch2 += i
    else:
        num.append(i)
        num2 += i

z = ' '.join(sorted(ch)+sorted(num))
z2 = ' '.join(sorted(ch2)+sorted(num2))
print('use list : ', z)
print('use string : ', z2)


c = 'h1t2p1s1'
res = ''
for i in c:
    if i.isalpha():
        x = i
    else:
        v = int(i)
        res = res + v*x
print(res) 
# o/p = 'https'

c2 = '4Y2H3K'
res2 = ''
for i in c2:
    if i.isdigit():
        d = int(i)
    else:
        x = i
        res2 += x*d
print(res2)
# o/p = 'YYYYHHKKK'

c3 = 'a3z4b2n5' 
res3 = ''
for i in c3:
    if i.isalpha():
        x = i
    else:
        d = int(i)
        res3 = res3 + x * d

print(''.join(sorted(res3)))
# o/p = 'aaazzzzbbnnnnn'
