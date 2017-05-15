# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        previous = dummy
        p1 = head
        p2 = head.next

        while p1 and p2:
            previous.next = p2
            p1.next = p2.next
            p2.next = p1
            p1, p2 = p2, p1
            previous = previous.next.next
            p1 = p1.next.next
            if p2.next != None:
                p2 = p2.next.next
            else:
                p2 = None

        return dummy.next
