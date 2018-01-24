# 2. Add Two Numbers
# Remember to use dummy head node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2
        if l2 == None:
            return l1

        dummy = ListNode(0)
        result = dummy

        carry = 0
        while l1 != None and l2 != None:
            temp = carry + l1.val + l2.val
            carry = int(temp / 10)
            result.next = ListNode(temp % 10)
            result = result.next
            l1 = l1.next
            l2 = l2.next

        if l1 == None:
            l1 = l2

        while l1 != None:
            temp = carry + l1.val
            carry = int(temp / 10)
            result.next = ListNode(temp % 10)
            result = result.next
            l1 = l1.next

        if carry != 0:
            result.next = ListNode(carry)

        return dummy.next
