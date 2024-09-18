# selection sort
def selection_sort(list1):
    for i in range(len(list1)):
        min_index = i
        for j in range(min_index+1, len(list1)):
            if list1[min_index] > list1[j]:
                min_index = j
        if i != min_index:
            list1[i],list1[min_index] = list1[min_index], list1[i]
    # return list1


if __name__=='__main__':
    testcases = [
        [27, 68, 43, 2, 19, 37, 6,15],
        [],
        [2,8,9,11,13,15,17],
        [-5,-23,-67,-39,-1,-11,-54],
        [2300,1000,1500,1800,600,1900],
        ['milan','zara','adidas','spencer','puma']
    ]
    for lists in testcases:
        selection_sort(lists)
        print(lists)
    