# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        curA = headA
        curB = headB

        numA = 0
        numB = 0

        while curA:
            numA += 1
            curA = curA.next

        while curB:
            numB += 1
            curB = curB.next

        if numA < numB:
            headA, headB = headB, headA
            numA, numB = numB, numA

        for i in range(numA - numB):
            headA = headA.next

        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
