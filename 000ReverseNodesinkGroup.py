# 25. Reverse Nodes in k-Group
# Very tricky about the pointers, be careful. 
# What pointer gets changed, what did not get changed.
# Four pointers: previous, head, end, after.
# First, reverse the nodes between head and end.
# Then, connect previous and after.
# Remember to reassign current to end after change. 


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return None
        if k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        current = dummy

        while current:

            previous = current
            head = current.next
            for i in range(k):
                if current.next:
                    current = current.next
                else:
                    return dummy.next

            end = current
            after = current.next

            (head, end) = self.reverse(head, end)

            previous.next = head
            end.next = after
            current = end 

        return dummy.next

    def reverse(self, head, end):

        if head.next == end:
            end.next = head
            return (end, head)

        previous = head
        current = head.next
        while current.next != end:
            next = current.next
            current.next = previous

            previous = current
            current = next

        next = current.next
        current.next = previous
        next.next = current

        return (end, head) 
