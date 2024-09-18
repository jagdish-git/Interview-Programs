# input_list = ['1','1.3','1.14','1.11']
# output = ['1', '1.3', '1.11', '1.14']
# sort as per len of str and after value


def sort_by_len(listx):
    new = []
    for n in range(len(listx)):
        for m in range(n, len(listx)):
            if len(listx[n]) > len(listx[m]):
                listx[n], listx[m] = listx[m], listx[n]
            elif len(listx[n]) == len(listx[m]):
                if float(listx[n]) > float(listx[m]):
                    listx[n], listx[m] = listx[m], listx[n]
    return listx


input_list = ['1.09','1.3','1.111','1.14','1.010','1.11','1', '1.01']
print(sort_by_len(input_list))

# procedure sorted and lambda
output = sorted(input_list, key= lambda x: (len(x),x))
print(output)