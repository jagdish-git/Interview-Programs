# shell sort
def shell_sort(arr):
    size = len(arr)
    gap = size//2
    
    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = anchor
        gap = gap // 2
    

if __name__ == '__main__':
    testcases = [
        [21, 38, 29, 17, 4, 25, 11, 32, 9],
        [2,1,5,7,2,0,5,1,2,9,5,8,3],
        [-4,-6,-32,-29,-1,-49,-8],
        ['chat-gpt','google-bard','bing-ai','github-copilot','wix-adi'],
        [4500,9077,2344,8912,9089,7068],
        [7,0,0,0,1],
        [2, 1, 5, 7, 2, 0, 5],
        [8]
        ]
    for elements in testcases:
        shell_sort(elements)
        print(elements)


# exercise : remove duplicates and also sort the array
def shell_sort_exercise(arr):
    size = len(arr)
    div = 2
    gap = size//div
    
    while gap > 0:
        index_to_delete = []
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= anchor:
                if arr[j-gap] == anchor:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor

        index_to_delete = list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for k in index_to_delete[-1::-1]:
                del arr[k]
        div = div * 2
        size = len(arr)
        gap = size // div


if __name__ == '__main__':
    element = [22,13,22,25,13]
    shell_sort_exercise(element)
    print(element)