# 142. Linked List Cycle II

# Tricky: check slow.next, fast.next and fast.next.next is not None.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        fast = head
        slow = head

        while slow.next and fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
            
        if not slow.next or not fast.next or not fast.next.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
