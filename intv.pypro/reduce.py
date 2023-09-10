# importing functools for reduce(function, sequence)
from functools import reduce
import operator

lis = [5, 8, 10, 20, 50, 100]

print(reduce(lambda x,y:x+y, lis)) # (((((5+8)+10)+20)+50)+100).
print(reduce(lambda x,y:x if x>y else y, lis)) # highest value in list
print(reduce(operator.add,["geeks", "for", "geeks"]))
print(reduce(operator.mul,lis))
print(reduce(operator.sub,lis))

