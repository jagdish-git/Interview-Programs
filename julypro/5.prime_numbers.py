# 1 ------
def prime_number_check(num):
    if num <= 1:
        print(f'{num} is not a prime number')
        return
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} Not Prime Number')
            break
    else:
        print(f'{num} Prime Number')
    
prime_number_check(83)

# 2 ------
def prime_numbers(many):
    strg = list()
    c = 0
    for n in range(100):
        if n > 1:
            for i in range(2,n):
                if n % i == 0:
                    break
            else:
                yield n
                c += 1

            if many <= c:
                break
    return strg

print(list(prime_numbers(10)))

# 3 ------
def prime_nonprime(listx):
    prim =[]
    nonprim = []
    for num in listx:
        if num <= 1:
            nonprim.append(num)
            continue
        for i in range(2, num):
            if num % i == 0:
                nonprim.append(num)
                break
        else:
            prim.append(num)      
        
    return prim, nonprim

lis = [22,3,4,-48,5,61,37,56,-78,87,91,7,8,77,-1,71,0,67,83]
print(prime_nonprime(lis))

# 4 -------