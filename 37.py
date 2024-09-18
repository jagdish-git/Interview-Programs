# Method 1: Using Slicing 
# this is reversing from the end index
def reverseArrayUptoK(input, k):

	print (input[:k+1] + input[:k:-1])

if __name__ == "__main__":
	input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	k = 3
	reverseArrayUptoK(input, k)
  # output : [1, 2, 3, 4, 9, 8, 7, 6, 5]


# Method 2: Using Two Pointers

def reverseArray(arr, k):
  start = k+1
  end = len(arr)-1
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
  return arr
arr=[1, 2, 3, 4, 5, 6, 7, 8]
k = 3
print(reverseArray(arr, k))
# output = [1, 2, 3, 4, 6, 5]


# reverse the from first index position of array
def reverseArrayUptoK(input, k):

	print (input[k-1::-1] + input[k:])

if __name__ == "__main__":
	input = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	k = 4
	reverseArrayUptoK(input, k)

# two pointers
def reverseArray2(arr, k):
    start = 0
    end = k-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr=[1, 2, 3, 4, 5, 6]
k = 4
print(reverseArray2(arr, k))
# output = [4, 3, 2, 1, 5, 6]



# argument slicing
def argument_reverse(arr, k):
    #   *args = arr[:k]
    pass

if __name__ == "__main__":
    arr=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 5
    argument_reverse(arr, k)