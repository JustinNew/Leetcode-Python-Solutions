# 86. Partition List

# Create two lists with dummy head and reconnect them again.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        small = ListNode(0)
        small.next = None
        d_s = small
        large = ListNode(0)
        large.next = None
        d_l = large

        while head:
            if head.val < x: 
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        small.next = d_l.next
        large.next = None
        return d_s.next
