#>>1
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1) # 5 * fact(4) * fact(3) * fact(2) * fact(1) * fact(0) = 120

print(fact(5))

#>>2
def facto(num):
    if num == 1 or num == 0:
        return 1
    res = 1
    while num > 0:
        res = res*num # 4*3*2*1 = 24
        num -= 1
    return res

print(facto(4))

#>>3
n = 6
i = 1
res1 = 1
while i <= n:
    res1 = res1*i # 1*2*3*4*5*6 = 720
    i += 1
print(res1)


#>>4

d = 7
res2 = 1
for i in range(d,0,-1): # (1,d+1) -- (1*2*3*4*5*6*7)
    res2 = res2*i # 7*6*5*4*3*2*1 = 5040       

print(res2)