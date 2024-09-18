# 1 -----
def palindrome_while(num):
    soln = ''
    if not num.isdigit() :
        for s in range(len(num),0,-1):
            soln += num[s-1]
        return "Palindrome String" if str(soln) == num else "Not palindrome String"
    temp = int(num)
    result = 0 
    while temp > 0:
        remainder = temp % 10
        result = result * 10 + remainder
        temp = temp // 10
    return f"{result} Palindrome Number" if result == int(num) else f"{result} Not palindrome number"

number = input('Enter number : ')
p = palindrome_while(number)
print(p)

# 2------
def palin(s):
    stor= result = ans = ''
    for i in range(1,len(s)+1):
        stor = stor + s[len(s)-i]
    for j in range(len(s),0,-1):
        result += s[j-1]
    for k in range(len(s)):
        ans = s[k] + ans
    if s == stor and s == result and s == ans:
        print(stor,'is palindrome')
    else:
        print(stor,'is Not palindrome')
    
palin('level')

# 3 ---------
def palin_while_string(string):
    ex = len(string)
    s = ''
    while ex > 0:
        s += string[ex-1]
        ex -= 1
    return f"{string} Palindrome String" if s == string else f"{string} Not palindrome String"
print(palin_while_string('helehj'))

# 4 --------
def palin_compare_both_side(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return f"{string} Not a Palindrome"
    return f"{string} is a palindrome"

print(palin_compare_both_side('1a2b3c4dd4c3b2a1'))

# 5 -------
def palin_comp_opp_site_whileloop(string):
    strln = len(string)
    i = 0
    while strln//2 > i:
        if string[i] != string[strln-i-1]:
            return False
        i += 1
    return True

print(palin_comp_opp_site_whileloop('9090932'))


# 6 -------
def palindrome_forloop(num):
    result = 0
    number = num
    for _ in range(len(str(number))):
        result = result*10 + number%10
        number //= 10
    return f"{num} is palindrome" if num == result else f"{num} not Palindrome"

print(palindrome_forloop(23232))