# 1: Half Pyramid Patterns in Python using Loop

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''
def half_pyramid(rows):
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print("*", end=' ')
        print()
    # for x in range(1,rows+1):
    #     print("* "*x)

# half_pyramid(5)

# 1.2 :  Inverted half Pyramid Patterns
'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''
def inverted_half_pyramid(rows):
    # for i in range(1, rows+1):
    #     for j in range(rows-i+1):
    #         print("*", end=' ')
    #     print()

    for i in range(rows, 0, -1):
        for j in range(i):
            print("*", end=' ')
        print()

# inverted_half_pyramid(5)

# 2: Patterns with Numbers
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
def pattern_number(rows):
    for i in range(1,rows+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
# pattern_number(5)


# 3. pattern with odd numbers
'''
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9
'''
def odd_num_pattern(rows):
    for i in range(1, rows+1):
        for j in range(1, i*2):
            if j%2 == 0:
                print(" ", end='')
            else:
                print(j, end='')
        print()

# odd_num_pattern(5)

# 4. print the pattern
'''

'''
def skip_one_postion_number(rows):
    for i in range(1, rows+1):
        num = 1
        for j in range(0, i):
            print(num, end=' ')
            num += 2
        print()
# skip_one_postion_number(5)





