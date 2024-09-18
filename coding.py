# check for the given string of parenthesis is balanced or not.
def balanced_parenthesis(strings):
    stack = []
    open = ['{', '[', '(']
    close = ['}', ']', ')']
    for paran in strings:
        if paran in open:
            stack.append(paran)
        elif paran in close:
            index = close.index(paran)
            if len(stack) > 0 and open[index] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return 'Unbalanced'

    return "Balanced Ok" if len(stack) == 0 else "Not Balanced"


def balanced_parenthesis_dict(stings):
    stack = []
    pdict = {"(": ')', "{": '}', "[": ']'}
    for bracket in stings:
        if bracket in pdict.keys():
            stack.append(bracket)
        elif bracket in pdict.values():
            if len(stack) == 0 or pdict[stack.pop()] != bracket:
                return "NotBalanced"

    return len(stack) == 0


def check_queue(mystr):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    dict1 = dict(zip(open_tup, close_tup))
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


if __name__ == "__main__":
    testcase = ["{[{(a)+(b)+(c)}]}",
                "[]",
                "",
                "}[()]{",
                "({]})",
                "a+b",
                "{[](){}()}{(["]
    # for test in testcase:
    #     print(balanced_parenthesis_dict(test))


def is_balanced(string):
    flag = True
    count = 0
    for p in string:
        if p == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            flag = False
            break
    if count != 0:
        flag = False

    return flag, count


# str1 = "()()()(())()"
# str2 = "(((((((())"
# str3 = ")))((("
# for i in str1, str2, str3:
#     print(is_balanced(i))


def brackets(expression):
    all_brackets = ['()', '[]', '{}']
    while any(x in expression for x in all_brackets):
        for br in all_brackets:
            expression = expression.replace(br, "")

    return not expression


# input_string = "({[{}]})"
# if brackets(input_string):
#     print(input_string, "balanced")
# else:
#     print(input_string, "Not balanced")


def two_sum(arr, targets):
    index_dict = {}
    for i in range(len(arr)):
        if targets - arr[i] in index_dict:
            return [index_dict[targets - arr[i]], i]
        index_dict[arr[i]] = i
    return []


# if __name__ == "__main__":
#     arrays = [2, 7, 9, 13, 6, 8]
#     target = 15
#     print(two_sum(arrays, target))

