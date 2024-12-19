# Pattern Programs
# 1. pyramid (full, with space)
'''  
    * 
   * *
  * * *
 * * * *
* * * * *
'''

def full_pyramid(row):
    for i in range(0, row):
        # for j in range(row-i-1):
        #     print(' ', end='')
        print(" "*(row-i-1), end='')
        for k in range(i+1):
            print("*", end=' ')
        print()

# full_pyramid(5)

# 2.fully pyramid(without any space)
'''
    *
   ***
  *****
 *******
*********
'''

def without_space_full_pyramid(row):
    for i in range(1, row+1):
        for j in range(row-i):
            print(' ', end='')
        for k in range(1,i*2):
            print('*', end='')
        print()

# without_space_full_pyramid(5)


#3. Pyramid Patterns in Python with Number
'''
    1
   123
  12345
 1234567
123456789
'''

def number_pyramid(rows):
    for i in range(1,rows+1):
        print(' '*(rows-i), end='')
        for k in range(1, i*2):
            print(k, end='')
        
        print()

# number_pyramid(5)

# 4. Pyramid Patterns in Python with Number with space 
'''
    1 
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
'''

def number_pyramid_space(rows):
    for i in range(1, rows+1):
        print(" "*(rows-i), end='')
        for k in range(1, i+1):
            print(k, end=' ')
        print()

# number_pyramid_space(5)


# 5. Inverted Full Pyramid Patterns in Python
'''
*********
 *******
  *****
   ***
    *
'''
def invert_pyramid(row):
    for i in range(row, 0, -1):
        print(' '*(row-i), end='')
        for j in range(1, i*2):
            print("*", end='')
        
        print()

# invert_pyramid(5)

# 6. Hollow Pyramid Patterns in Python
'''
    *    
   * *   
  *   *  
 *     * 
*********
'''

def hollow_pyramid(rows):
    # for i in range(1, rows+1):
    #     for k in range(1, rows*2):
    #         if k == rows-i+1 or k == rows+i-1 or i == rows:
    #             print(k, end='')
    #         else:
    #             print(' ', end='')
    #     print()

    for i in range(1,rows):
        print(" "*(rows-i), end='')
        for k in range(1, i+1):
            if k == 1 or k == i:
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()
    for j in range(1,rows*2):
        print("*", end='')

# hollow_pyramid(5)


