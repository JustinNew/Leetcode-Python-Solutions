# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        start = head
        if head == None:
            return head

        previous = head
        current = head.next

        while current:
            if previous.val != current.val:
                previous = current
                current = current.next
            else:
                previous.next = current.next
                current = current.next

        return start
