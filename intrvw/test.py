def fibonacci(n):
    a,b = 0,1
    rev_list = []
    for _ in range(n):
        rev_list.append(a)
        a, b = b, a+b

    return rev_list[::-1]


f = fibonacci(10)
print(f)