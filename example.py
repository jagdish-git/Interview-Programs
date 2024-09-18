# name1 = 'jagdish'
# name2 = 'bal'

# for i in range(1,50):
#     if i%3 == 0:
#         print(name1)
#     elif i%5 == 0:
#         print(name2)
#     elif i%3 == 0 and i%5 == 0:
#         print(name1+name2)
#     else:
#         print(i)



lis = [{"name":"ABC","marks":70},{"name":"PQR","marks":40},
{"name":"ZYX","marks":60},{"name":"PCB","marks":50},{"name":"EFG","marks":60}]

print (sorted(lis, key = lambda i: i['marks']))
# print (sorted(lis, key = lambda i: (i['marks'],i['name'])))
# print (sorted(lis, key = lambda i: i['marks'],reverse=True))

# bubble_sort method

def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


elements = [
            { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
            { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
            { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
            { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]

bubble_sort(elements)
print(elements)

#By using ITEM GETTER

from operator import itemgetter

print(sorted(lis, key=itemgetter('marks')))


# import json
# import requests

# url = requests.get('https://api.postalpincode.in/pincode/400097')

# st = url.json()

# for i in st:
#     for j in range(len(i['PostOffice'])):
#         print(i['PostOffice'][j].get('District'))
