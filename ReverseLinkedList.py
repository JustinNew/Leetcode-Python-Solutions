# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

p    c    n
NULL 1 -> 2 -> 3 -> 4 -> 5 -> NULL

                            p   c
NULL <- 1 <- 2 <- 3 <- 4 <- 5  NULL
'''

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None
        elif not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cur = head
        prev = dummy
        while cur.next:
            next = cur.next
            if cur == head:
                cur.next = None
            else:
                cur.next = prev

            prev = cur
            cur = next

        cur.next = prev
        dummy.next = cur

        return dummy.next

    ########################################################################################################
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
    
        return prev
