# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i-1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = anchor
    return arr

if __name__ == '__main__':
    testcases = [
        [11,9,29,7,2,15,28],
        [],
        [-4,-6,-32,-29,-1,-49,-8],
        ['chat-gpt','google-bard','bing-ai','github-copilot','wix-adi'],
        [4500,9077,2344,8912,9089,7068],
        [7,0,0,0,1],
        [2, 1, 5, 7, 2, 0, 5]
        ]
    for elements in testcases:
        insertion_sort(elements)
        # print(elements)


# exercise: running median of sequnce numbers.
# if even number list then choose two middle number and find out the average
# if its odd number then choose only the middle number

def place_to_insert(array, key):
    index = 0
    for i in array:
        if i > key:
            break
        else:
            index += 1
    return index


def insert_to_sorted(array, key):
    index = place_to_insert(array, key)
    return array[0:index]+[key]+array[index:]


if __name__ == "__main__":
    array = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]

    stream = []
    n = 0
    count = 0
    while len(array) > n:
        i = array[count]
        count += 1
        stream = insert_to_sorted(stream, i)
        if count % 2 == 1:
            print(f"Median of {stream} : {stream[(count)//2]}")
        else:
            i1 = count//2
            i2 = (count//2) - 1
            print(f"Median of {stream} : {(stream[i1] + stream[i2])/2}")
        n += 1