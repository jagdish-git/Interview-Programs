#>>1(in a range of 1000)

def amst(n):
    stor = []
    for x in range(10,n):
        # if x > 10:
        ln = len(str(x))
        temp = x
        res = 0
        while temp > 0:
            d = temp % 10
            res = res + d**3
            temp = temp // 10
        if x == res:
            stor.append(res)
    return stor

print(amst(1000)) #[153, 370, 371, 407]


#>>2 (check amstrong or not)

def amstr(n):
    temp = n
    ln = len(str(n))
    res = 0 
    while temp > 0:
        res = res + ((temp%10)**ln)
        temp //= 10
    
    if res == n:
        print(n, 'is an amstrong number')
    else:
        print(n, 'is NOT an amstrong number')

amstr(371)

#>>3(for loop)
def amstron(m):
    for temp in range(10,m):
        ln = len(str(temp))
        res = 0
        for i in str(temp):
            res = res + int(i)**ln

        if res == temp:
            print(temp, 'is an amstrong number')
        # else:
        #     print(temp, 'is NOT an amstrong number')

amstron(2000)
