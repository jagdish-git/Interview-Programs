list1 = [1,2,3,4,5,6,7,8,9]

*args, last = list1

print(list1)
print(*args)
print(args)

result = *args[::-1], last
result2 = args[::-1],last

print('Result *', list(result))
print('Result ', list(result2))