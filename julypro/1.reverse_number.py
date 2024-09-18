# 0 ------
def reverse_inbuilt(number):
    method_slice = str(number)[::-1]
    method_reversed = ''.join(reversed(str(number)))
    return int(method_slice), int(method_reversed)

number2 = 797536
print(reverse_inbuilt(number2))
# 1 ------
def reverse_number(number):
    # temp = number
    result = 0
    while number > 0:
        digit = number % 10
        result = result*10 + digit
        number //= 10
    return result

num = 9861482
r = reverse_number(num)
print('The reversed Number :',r)

# 2 -------
def reverse_number_forloop(number):
    str_number = str(number)
    storage = result = solution = ""
    for n in str_number:
        storage = n + storage

    for m in range(len(str_number),0,-1):
        result += str_number[m-1]
    
    for i in reversed(str_number):
        solution += i 
    return int(storage), int(result), int(solution)

for_num = 897861257
r2 = reverse_number_forloop(for_num)
print('For loop reverse number :',r2)

# 3 -------
nums = 234578
results = 0
def rever_recusion(number):
    global results
    if number > 0:
        results = results * 10 + number%10
        rever_recusion(number//10)
    return results
print('Revesed Recursion :',rever_recusion(nums))
