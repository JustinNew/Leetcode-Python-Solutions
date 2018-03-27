# 61. Rotate List
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Corner cases:
# 1. k = 0
# 2. head = None
# 3. Total nodes number smaller than k.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head == None:
            return head

        count = 1
        p1 = head
        while p1.next:
            count += 1
            p1 = p1.next

        k = k % count

        p1 = head
        p2 = head
        p2prev = None

        for i in range(k):
            p1 = p1.next
            if p1 == None:
                return head

        while p1.next != None:
            p2prev = p2
            p2 = p2.next
            p1 = p1.next

        p1.next = head
        head = p2
        p2prev = None

        return head
