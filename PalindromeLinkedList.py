# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # Get the number of nodes.
        n = head
        count = 0
        while n:
            count += 1
            n = n.next

        if count <= 1:
            return True

        # Get the middle head.
        mid = int(count / 2)
        n = head
        for i in range(mid):
            n = n.next
        if count % 2 == 1:
            n = n.next

        # Reverse the second half.
        dummy = ListNode(0)
        dummy.next = n

        prev = dummy
        cur = n
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        n = prev

        # Compare the two half.
        for i in range(mid):
            if head.val != n.val:
                return False
            head = head.next
            n = n.next

        return True    
