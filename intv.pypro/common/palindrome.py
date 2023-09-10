# Palindrom String

def palin(s):
    stor = ''
    for i in range(1,len(s)+1):
        stor = stor + s[len(s)-i]
    if s == stor:
        print(stor,'palindrome')
    else:
        print(stor,'Not palindrome')
    
palin('leveld')


st = 'madams'
if st == st[::-1]:
    print(st,' is palindrome')
else:
    print(st,'not palindrome')


s = 'hanah'
if s == ''.join(reversed(s)):
    print(s,'is palindrome')
else:
    print(s,'is not palindrome')

strn = 'kutudk'
res = ''
ln = len(strn)
while ln>0:
    res = res + strn[ln-1]
    ln = ln - 1

print(res == strn)

def palindrom(string):
    ln = len(string)
    for i in range(ln):
        if string[i] != string[ln-i-1]:
            return False
    return True 

strx = 'NITIN'
print(palindrom(strx))

def palin_while(string):
    first = 0
    last = len(string)-1
    while first < last :
        if string[first] == string[last]:
            first += 1
            last -= 1
        else:
            return 'Not palindrom'
    return f'{string} is plaindrom'

print(palin_while('momom'))

#Palindrom Number 

def palind(num):
    temp = num
    sm = 0
    while temp > 0:
        d = temp % 10
        sm = sm*10 + d
        temp = temp // 10
    
    if sm == num :
        print(num,'is palindrome number')
    else:
        print(num,'is not palindrome number')

palind(121)


num = 3434
if str(num) == str(num)[::-1]:
    print(num,'is palindrome number')
else:
    print(num,'is not palindrome number')


print('>>>>>>>>>>>>>>>>>>>>')
# Q./check positive or negative integer is palindrome or not?/

def palin_negative(num):
    temp = abs(num)
    summ = 0
    while temp > 0:
        digit = temp % 10
        summ = summ*10 + digit
        temp = temp // 10
    print(summ)
    if -summ == num:
        return True
    else:
        return False

num = -12121
print(palin_negative(num))