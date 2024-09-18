def sort_by_word(strs):
    splt = strs.split()
    i = 0
    while i < len(splt)-1:
        if len(splt[i]) > len(splt[i+1]):
            splt[i], splt[i+1] = splt[i+1], splt[i]
            i = -1
        i += 1
    return ' '.join(splt)


def word_len_sorted(str1):
    # splt= str1.replace(',','').split()
    return ' '.join(sorted(str1.split(), key=len))


str1 = 'Prasnna interviwing Jagdish, If Jagdish qualify He will be move to final round'
print(sort_by_word(str1))
print(word_len_sorted(str1))




# Define the string
string = 'Prasnna interviwing Jagdish, If Jagdish qualify He will be move to final round'

# Remove the comma from the string and split into words
words = string.replace(',', '').split()

# Function to sort words by length using bubble sort
def bubble_sort_by_length(words):
    n = len(words)
    for i in range(n):
        for j in range(n - i - 1):
            if len(words[j]) > len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]

# Sort the words using bubble sort
bubble_sort_by_length(words)

# Join the sorted words back into a string
sorted_string = ' '.join(words)
sorted_string
