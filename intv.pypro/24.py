from operator import itemgetter


def dict_sort(dictx):
    new_dict = {k:v for k,v in sorted(dictx.items(), key=lambda x:x[1])}
    sorted_dict = dict(sorted(dictx.items(), key= lambda i:i[1]))
    itemget_dict = dict(sorted(dictx.items(), key=itemgetter(1)))
    print(new_dict, '\n', sorted_dict, '\n',itemget_dict)
    sorted_dict_desc = dict(sorted(dictx.items(), key= lambda i:i[1], reverse=True))
    print(sorted_dict_desc)

x = {1: 2, 3: 4, 4: 3, 2: 1, 6: 0, 8: 5}
dict_sort(x)