a=15
# % for remainder
if a%2 == 0:
    print("even")
# / to get quotient ansr= 7.5 it gives with .value also 5.5, 6.5
print(a/2)
# // to get quotient ansr= 7 it gives without .value  5, 6
print(a//2)
# reverse a string
a = "rotatoru"
b = a[::-1]
if a==b:
    print("palindrome")
else:
    print("Not")

new_rev_str = ''
for each in a:
    new_rev_str = each + new_rev_str
if a==new_rev_str:
    print("palindrome")
else:
    print("Not")

#find the missing number

a = [2,3,4,5,6,7,8]
n = 8
sum1 = sum(a)
expec_sum = n*(n+1)//2
num = expec_sum-sum1
print(num)

#factorial  
n = 5
fact = 1
for each in range(1, n+1):
    fact = fact*each
print(fact)

#Intersection
lst1 = list(set([15, 9, 10, 56, 23, 78, 5, 4, 9]))
lst2 = list(set([9, 4, 5, 36, 47, 26, 10, 45, 87]))
new_list = []
for each in lst1:
    if each in lst2:
        new_list.append(each)
print(new_list)

a = [15, 9, 10, 56, 23, 78, 5, 4, 9]
b = list(set(a))

#find the second largest element in an array
a = [15, 9, 10, 56, 23, 78, 78, 5, 4, 9]
a = list(set(a))
a.sort()
b = sorted(a)
print(a)
print(f"second Largest element is {a[-2]}")

# longest substring

a = "abcabcbb"
map = {}
char_list = []
sub_str = ''
count = 0
for each in a:
    if each not in char_list:
        char_list.append(each)
        sub_str = sub_str+each
        count = count + 1
    elif each in char_list:
        map[sub_str] = count
        sub_str = ""
        sub_str = sub_str + each
        count = 1
        char_list = []
        char_list.append(each)

map[sub_str] = count
values = map.values()
max = max(values)
print(max)

#fibonacci
a = 0
b = 1
c = 1
n = 9
for i in range(2, n+1):
    c = a+ b
    a =b
    b = c
print(c)


def is_valid(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_map:
            if not stack or stack[-1] != bracket_map[char]:  # Check if it matches the last opened bracket
                return False
            stack.pop()  # Pop the last opened bracket
        else:
            stack.append(char)  # It's an opening bracket, push to stack

    return not stack  # If stack is empty, all brackets were properly closed

# Test the function
a = "{{[()]}}"
print(is_valid(a))  # Output: False

a = {"k1": "v2", "v1":"k2", "k3":"v4", "v3":"k4"}
o_p = [["k1", "k2", "k3", "k4"], ["v1", "v2", "v3", "v4"]]
list_1 =[]
list_2 = []
for i,each in enumerate(a):
    val = a.get(each)
    if i== 0 or i%2 == 0:
        list_1.append(each)
        list_2.append(val)
    else:
        list_2.append(each)
        list_1.append(val)
print(f"list1: {list_1} and list2: {list_2}")

class Dog:

    # A simple class
    # attribute
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

a = "aaabbbcddcabeerr"
intial_str = a[0]
prev_str = a[0]
print(a[0])
count = 0
final_str = ''
for each in a:
    if each == intial_str:
        count += 1
    elif each != intial_str:
        final_str = final_str + intial_str + str(count)
        count = 1
        intial_str = each
final_str = final_str + intial_str +str(count)
print(f"final str:: {final_str}")


alphabets = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q"
             "r", "s", "t", "u", "v", "w", "x", "y", "z")

for each in range(1, 26+1):
    if each%3 == 3:
        print(f"value with remainder 3 is:: {alphabets[each-1]}")
#pyramid pattern
n= 6
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
    print()

# Write a program to print the given number is odd or even.

h = 5

if h%2==0:
    print("even")
else:
    print("odd")

# Write a program to check if the given number is palindrome or not
num = 12321
temp =  num
reverse = 0

while temp>0:
    remainder = temp%10
    reverse = (reverse*10) + remainder
    temp = temp//10
if reverse == num:
    print("palindrome")
else:
    print("not palindrome")

# Write a program to check if the given number is Armstrong or not.

num = 1253
temp = num
sum_value = 0
list_d =  []
while temp>0:
    remainder = temp%10
    print(f"remainder {remainder}")
    list_d.append(remainder)
    temp =temp//10
    print(f"temp {temp}")
for each in list_d:
    sum_value =  sum_value + each ** len(list_d)
print(f"sum Value :: {sum_value}")

#Write a program to find a fibonacci of a number.
a = 0
b = 1
num = 9
list_values = []
for each in range(2, num+1):
    c=a+b
    a = b
    b = c
    list_values.append(c)
print(list_values)

# Write a program to print the following pattern.
# *
# * *
# * * *
# * * * *
# * * * * *
n = 5
for each in range(1, n+1):
    print("* "*each)

# Write a program to print the following pattern.
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
n = 5
for each in range(1, n+1):
    for j in range(n-each):
        print(end=" ")
    for l in range(each):
        print("* ", end="")
    print()

# Write a program to print the following pattern.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = 5
for each in range(1, n+1):
    for j in range(1, each+1):
        print(f"{j} ", end="")
    print()

# Write a program to print the following pattern.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
n = 5
num = 1
for each in range(1, n+1):
    for j in range(1, each+1):
        print(f"{num} ", end="")
        num = num+1
    print()

# Write a program to print the following pattern.
# A
# B B
# C C C
# D D D D
# E E E E E
n = 5
string = "ABCDE"
for i, each in enumerate(string):
    for j in range(0, i+1):
        print(each, end=" ")
    print()

def alphapat(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1

        print("\r")


n = 5
alphapat(n)

# Write a program to print the following pattern.
# A
# B C
# D E F
# G H I J
# K L M N O
num = 65
n = 5
for each in range(0, n):
    for j in range(each+1):
        ch = chr(num)
        print(ch, end=" ")
        num = num + 1
    print()

a = [1,34,5,6,76,78,9,8]
# a.sort()
# print(a)
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)


# Recurssion
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

val = fact(5)
print(val)

# Recursive function
# it is a process in which a function calls itself directly or indirectly.
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
    print(recursive_fibonacci(i))

# Write a Python function that reads a text file and prints each line to the console.
def read_func(path):
    with open(path, "r") as file:
        for each in file:
            print(each)

read_func("sample.txt")
# Write a program that takes a list of strings and writes them to a file, with each string on a new line
list_of_strings = ["Test File", "Test2 File", "File Operations"]
with open("sample1.txt", "w") as file:
    for each in list_of_strings:
        file.write(each+"\n")
# Modify the program in the previous question so that it appends the list of strings to the file instead of overwriting it.
with open("sample1.txt", "a") as file:
    for each in list_of_strings:
        file.write(each + "\n")

# Function to read emails from a file and return a set of emails
def read_emails_from_file(filename):
    with open(filename, 'r') as file:
        emails = set(line.strip() for line in file)  # Using set to remove duplicates and strip newline
    return emails

# Reading emails from both files
amazon_emails = read_emails_from_file('amazon_ordered.txt')
flipkart_emails = read_emails_from_file('flipkart_ordered.txt')

# Finding common emails between the two sets
common_emails = amazon_emails.intersection(flipkart_emails)

# Printing the common emails
print("Common emails in both files:")
for email in common_emails:
    print(email)


def new_func(func):
    def wrapper(a,b):
        print("inside new func")
        add = a + b
        sub = func(a, b)
        return add, sub
    return wrapper

def new_func1(func):
    def wrapper(a,b):
        print("inside new func1111")
        mul = a * b
        add, sub = func(a, b)
        return mul, sub, add
    return wrapper
@new_func1
@new_func
def func(a, b):
    sub = a - b
    return sub

mul, sub, add =  func(6,3)
print(f"mul::{mul}add::{add}:::sub {sub}")

#Iterator

class Iterators:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a<=5:
            x = self.a
            self.a = self.a+1
            return x
        else:
            raise StopIteration
itr = Iterators()
my = iter(itr)
for x in my:
    print(x)

#generators

def generator(val):
    n= 1
    while n<=val:
        yield 2**n
        n =  n+1
a = generator(6)
for each_val in a:
    print(f"Generator:: {each_val}")

mail = "my.ownsite@our-earth.org"
pattern = "[a-zA-Z0-9-_+\.]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}"
import re
find = re.match(pattern, mail)
if find:
    print("exists")

text = "Contact me at 9398545933 or +91-9398545933"
pattern = "\+?\d{1,2}-?\d{1,10}|\d{1,10}"
matches = re.findall(pattern, text)
#Ipaddress pattern
ip_add_ptrn = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

for match in matches:
    print("Found phone number:", match)

text = "Contact me at +1-800-555-1234 or 800-555-1234"
pattern = r'\+?\d{1,2}-\d{3}-\d{3}-\d{4}'
matches = re.findall(pattern, text)

for match in matches:
    print("Found phone number:", match)

text = "Check out https://example.com and http://another-example.com"
pattern = r'https?://[a-zA-Z0-9./-]+'
urls = re.findall(pattern, text)

for url in urls:
    print("Found URL:", url)

post = "Loving the #Python community! #coding_is_fun #regex"
op = ['#Python', '#coding_is_fun', '#regex']
pattern = "#[a-zA-Z]+"
val = re.findall(pattern, post)
print(val)

test_dates = [
    "01-01-2000", "15-07-2023", "31-12-2099", "29-02-2000",
    "32-01-2023", "15-13-2023", "01-01-1899", "31-04-2023",
    "29-02-2023", "00-10-2023", "15-00-2023", "31-11-2023",
    "15-12-2100"
]

pattern = "(0[1-9]|1[0-9]|2[0-9]|3[0-1])-(0[1-9]|1[0-2])-(19|20)\d{2}$"


for date in test_dates:
    if not re.match(pattern, date):
        print("Not True")
    else:
        print("True")

input_text = "Alice went to the Wonderland. Bob and Charlie joined her."
pattern = r"\b[A-Z]+[a-z]+"
val =  re.findall(pattern, input_text)
print(val)