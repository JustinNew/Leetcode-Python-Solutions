# 86. Partition List

# Use dummy head node
# Create two lists, one for smaller and one for larger or equal
# Combine the two lists together

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def partition(self, head, x):

        if not head:
            return None

        small = ListNode(0)
        large = ListNode(-1)
        small_head = small
        large_head = large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None    # Need to handle this dangling next pointer.
        small.next = large_head.next
        return small_head.next

    # Another solution.
    # Also need to deal with the dangling next pointer. 
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head:
            return None

        small = ListNode(0)
        large = ListNode(-1)
        small_head = small
        large_head = large

        while head:
            if head.val < x:
                small.next = head
                head = head.next
                small = small.next
                small.next = None
            else:
                large.next = head
                head = head.next
                large = large.next
                large.next = None

        small.next = large_head.next
        return small_head.next
