str1 = "{()[]}[{}]"
str2 = "[(]){}([])"
str3 = "[{()}][()]"
str4 = "[{(])}][({)]"
str5 = "][)()}{"

# method 1
def check_stack(strn):
    stack = []
    open_list = ['(','[','{']
    close_list = [')',']','}']
    for i in strn:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if (len(stack) > 0) and open_list[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                return 'UN-Balanced'
    if len(stack) == 0:
        return 'Balanced'
    else:
        return 'Unbalanced'

# for i in str1,str2,str3,str4:
#     print(i, '-', check_stack(i))


# method 2

def check_queue(mystr):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    dict1 = dict(zip(open_tup,close_tup))
    queue = []

    for i in mystr:
        if i in open_tup:
            queue.append(dict1[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return 'unBalanced'
    if not queue:
        return "balanced"
    else:
        return 'Unbalanced'

# for i in str1,str2,str3,str4:
#     print(i, '-', check_queue(i))


# method 3
def check_stack_dict(strn):
    stack = []
    brackets = {"{":'}', "[":']', "(":')'}
    for char in strn:
        if char in brackets.keys(): # or ['{', '[','(']
            stack.append(char)
        else:
            if stack:
                top = stack.pop()
                if brackets[top] != char:
                    return 'Wrong Pop- No'
            else:
                return 'Empty Stack- No'
    return 'No' if stack else 'Yes'


# for i in str1,str2,str3,str4,str5:
#     print(i, ':', check_stack_dict(i))


# method 3.1(similar)
def check_stack_dict_2(strn):
    stack = []
    brackets = {"{": '}', "[": ']', "(": ')'}
    for char in strn:
        if char in ['{', '[','(']:
            stack.append(char)
        else:
            if len(stack) == 0 or char != brackets[stack.pop()]:
                return False
    return len(stack) == 0 

# for i in str1,str2,str3,str4,str5:
#     print(i, ':', check_stack_dict_2(i))

# method 4(dummy method)
def balanced(strn):
    stack = []
    for char in strn:
        if char in ['{', '[','(']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False
            if current_char == '(':
                if char != ')':
                    return False
    if len(stack) == 0 :
        return True
    else:
        return False


for i in str1,str2,str3,str4,str5:
    print(i, ':', balanced(i))