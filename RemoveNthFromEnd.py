# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head == None:
            return None

        start = head
        count = 1

        while start.next != None:
            count += 1
            start = start.next

        if count < n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        current = head
        previous = dummy
        for i in range(count-n):
            current = current.next
            previous = previous.next

        previous.next = current.next

        return dummy.next 
