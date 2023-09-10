# summation of factorial number
# 145! = 1! +4! +5! = 1+24+120= 145

# 1. While Loop

def sum_fact(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp%10
        res = 1
        while digit > 0:
            res = res * digit
            digit -= 1
        temp = temp // 10
        sum = sum + res

    if sum == num:
        return True
    else:
        return False

s = sum_fact(145)
print('WhileLoop - {}'.format(s))


# 2. For Loop
def summation(num):
    sum = 0
    for d in str(num):
        res = 1
        for i in range(1,int(d)+1):
            res = res * i
        sum = sum + res
    if sum == num:
        return True
    else:
        return False

s = summation(145)
print('ForLoop - {}'.format(s))

# interval of 1 to n 

def sum_fact_range(start, end):
    for num in range(start,end):
        temp = num
        sum = 0
        while temp > 0:
            digit = temp%10
            res = 1
            while digit > 0:
                res = res * digit
                digit -= 1
            temp = temp // 10
            sum = sum + res

        if sum == num:
            print(num) 


sum_fact_range(1,200000)
# o/p - 1,2, 145, 40585