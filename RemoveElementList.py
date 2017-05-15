# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head == None:
            return None

        previous = None
        current = head
        head = None
        while current:
            if current.val == val:
                current = current.next
                if previous:
                    previous.next = current
            else:
                if not previous:
                    head = current
                previous = current
                current = current.next
 
        return head

def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    # Remove the heading nodes
    while head and head.val == val:
        head = head.next
    if not head:
        return head
    prev, cur = head, head.next
    while cur:
        while cur and cur.val == val:
            cur = cur.next
        prev.next = cur
        if cur:
            prev, cur = prev.next, cur.next
    return head
