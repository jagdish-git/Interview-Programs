# filter(function, sequence)
#   function: function that tests if each element of a sequence true or not.
#   sequence: sequence which needs to be filtered, it can 
#   be sets, lists, tuples, or containers of any iterators.

#1
def fun(var):
    vowels = ['a','e','i','o','u']
    if var in vowels:
        return var
    else:
        return False

str1 = 'containers'
f = filter(fun, str1)
print(list(f))


#2
print(list(filter(lambda x:x%2!=0, [3,5,2,7,8,9,4,6,1])))