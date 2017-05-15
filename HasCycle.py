# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None:
            return False

        p1 = head
        p2 = head.next

        while True:

            if p1 is None or p2 is None:
                return False
            elif p1 == p2:
                return True
            else:
                p1 = p1.next
                if p2.next != None:
                    p2 = p2.next.next
                else:
                    return False 

