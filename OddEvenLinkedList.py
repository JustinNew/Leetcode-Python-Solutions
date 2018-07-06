# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        n_h = head

        even = ListNode(0)
        even_h = even

        count = 0
        prev = None
        while head:
            count += 1
            if count % 2 == 1:
                if prev:
                    prev.next = head
                prev = head
            else:
                even.next = head 
                even = even.next
            head = head.next
        even.next = head
       
        prev.next = even_h.next
        return n_h 
