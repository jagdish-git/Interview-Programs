# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
# Explanation: 9999999+9999 = 10009998

def add_two_numbers(l1,l2):
    result = []
    carry = 0
    for n in range(max(len(l1),len(l2))):
        digit1 = l1[n] if n < len(l1) else 0
        digit2 = l2[n] if n < len(l2) else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        result += [total % 10]
    if carry:
        result += [carry]
    return result


if __name__ == '__main__':
    testcases = [([2, 4, 3], [5, 6, 4]),
                ([0],[0]),
                ([9,9,9,9,9,9,9], [9,9,9,9]),
                ([8,9,6],[4,5,7]),
                ([9,9],[1]),
                ([0,1],[0,1,3]),
                ([],[0,6])]
    
    for tups in testcases:
        print(add_two_numbers(tups[0], tups[1]))
