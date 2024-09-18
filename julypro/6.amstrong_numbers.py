# 1 -----
def amstrong_ina_range(rage):
    all_amst = []
    for number in range(1,rage):
        if number >= 100:
            temp = number
            res = 0
            while temp > 0:
                digt = temp % 10
                res = res + digt**len(str(number))
                temp = temp // 10
            if res == number:
                all_amst.append(number)


    return all_amst

print(amstrong_ina_range(2000))
#[153, 370, 371, 407, 1634, 8208, 9474] -- in between (100-10,000)

# 2 ------
def amstrong_forloop(nums):
    for num in range(nums):
        if num > 100:
            ln = len(str(num))
            res = 0
            for i in str(num):
                res += int(i)**ln
            if res == num:
                print(f'{num} is a amstrong number !!')

amstrong_forloop(1000)

# 3 ------
def amstrong_forloop_check(num):
    if num < 100:
        return None
    ln = len(str(num))
    res = 0
    for i in str(num):
        res += int(i)**ln

    if res == num:
        print(f'{num} is an Amstrong number !!')
    else:
        print(f'{num} is NOT an amstrong number !!')

amstrong_forloop_check(9474)