test_str = 'geeksforgeeks_is_best_for_geeks'

# Using split() + join() + title() + generator expression
def camel_case(str1):
    split_str = str1.split('_')
    result_str = split_str[0] +''.join(i.title() for i in split_str[1:])
    return result_str

c = camel_case(test_str)
print(c)  #geeksforgeeksIsBestForGeeks


# Using split() + join() + title() + map()

def camel_case_map(str1):
    first, *baki =  str1.split('_')
    res = ''.join([first.lower(), *map(str.title,baki)])
    print(res)

camel_case_map(test_str)