# Add Two Numbers in Python leetcode:2
# [2,4,3] + [5,6,4] = [7, 0, 8] 


def add_two_numbers(list1, list2):
    result = []
    carry = 0
    for number in range(max(len(list1), len(list2))):
        digit1 = list1[number] if number < len(list1) else 0
        digit2 = list2[number] if number < len(list2) else 0

        total =  digit1 + digit2 + carry
        carry = total // 10
        
        result.append(total % 10)

    if carry:
        result.append(carry)

    return result


if __name__ == '__main__':
    testcases = [([2, 4, 3], [5, 6, 4]),
                ([0],[0]),
                ([9,9,9,9,9,9,9], [9,9,9,9]),
                ([8,9,6],[4,5,7]),
                ([9,9],[1]),
                ([0,1],[0,1,3]),
                ([],[0,6])]

    for listx in testcases:
        print(add_two_numbers(listx[0],listx[1]))


# As per LeetCode, Linked list method

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while (l1 != None or l2 != None) or carry:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next
    
# s = Solution()
# s.addTwoNumbers([3,4,2],[5,6,4])