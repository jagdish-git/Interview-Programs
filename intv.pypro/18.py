# Second Largest Number
# 1. without using any builtin method (recommended)

def second_largest(n):
    if n[0] > n[1]:
        first = n[0]
        second = n[1]
    else:
        first = n[1]
        second = n[0]
    for i in range(2, len(n)):
        if n[i] > first:
            second = first
            first = n[i]
        elif n[i] > second and n[i] != first:
            second = n[i]
    print(second)

list1 = [7,22,35,65,42,11,3,29,58,65]
second_largest(list1)


# 2. reverse sort

def rev_sort(list):
    list.sort(reverse=True)
    print(list[1])

list2 = [7,22,35,65,42,11,3,29,58]
rev_sort(list2)

# 3. Set and Max

def max_set(list):
    new_set = set(list)
    print(new_set)
    new_set.remove(max(new_set))
    print(new_set)
    print(max(new_set))

max_set(list2)


# 4. indexing

print(list2[-2])