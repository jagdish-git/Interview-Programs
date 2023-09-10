# 1.>>
def prime_range(m,n, limit):
    x = []
    c = 0 
    for i in range(m,n):
        if i > 1:
            for j in range(2,i):
                if i%j == 0:
                    # x.append(i)
                    break
            else:
                x.append(i)
                c += 1
            if c >= limit:
                break
    return x

p = prime_range(100,200, 12)
print(p)

#2.>>
def prime_number(n):
    if n > 1:
        for j in range(2,n):
            if n%j == 0:
                print(n,'is a non-prime')
                break
        else:
            print(n,'is a prime number')

prime_number(41)

#3.>>
lis = [22,3,4,5,61,37,56,87,91,7,8,77,71,67,83]
prm = []
non = []
for i in lis:
    for j in range(2,i):
        if i % j == 0:
            non.append(i)
            break
    else:
        prm.append(i)

print('Prime', prm)
print('Non-Prime', non)

#4.>>
def prime_flag(num):
    flag = False
    if num > 1:
        for i in range(2,(num//2)+1):
            if num%i == 0:
                flag = True
                break
    if flag:
        return '---Not Prime---'
    else:
        return '---Prime---'

print(prime_flag(1))


input = {'a': 1,'b':2, 'c':{'d':5,'e':6}}
output = {'a':1,'b':2,'c_d':5,'c_e':6}
new = {}

for i,j in input.items():
    if type(j) == dict:
        # print(i,j)
        for k,l in j.items():
            # print({'_'.join(i+k):l})
            new.update({'_'.join(i+k):l})
    else:
        new.update({i:j})

print(new)

