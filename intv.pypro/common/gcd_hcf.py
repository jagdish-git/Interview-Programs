import math

#>>1
print(math.gcd(60,30))

#>>2
def gcd(a,b):

    res1 = []
    res2 = []
    res3 = []
    for itr in range(1,a+1):
        if a % itr == 0:
            res1.append(itr)
    for itr2 in range(1,b+1):
        if b % itr2 == 0:
            res2.append(itr2)
    
    res3 = set(res1).intersection(res2)

    return max(res3)

print(gcd(24,30))

#>>3
num1 = 36
num2 = 60
gcdn = 1
for i in range(1, min(num1,num2)):
    if (num1 % i == 0) and (num2 % i == 0):
        gcdn = i

print(gcdn)


#>>4
def gcd2(a,b):
    if b == 0:
        print('b--->',b)
        return a
    print('a--->',a,b)
    return gcd2(b, a%b)

print(gcd2(24,30))


#>>5

def hcf(num1,num2):
    while num1 != num2:
        if num1 > num2:
            num1 =num1 - num2
        else:
            num2 =num2 - num1
    return num1
    
num1 = 36
num2 = 60
print("Hcf of", num1, "and", num2, "is",hcf(num1,num2))