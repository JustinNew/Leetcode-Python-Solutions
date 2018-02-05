# 92. Reverse Linked List II

# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# return 1->4->3->2->5->NULL.
# Note: 1 ≤ m ≤ n ≤ length of list.

# Tricky about return head node if m == 1.

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        count = 0
        p1 = head
        while p1:
            p1 = p1.next
            count += 1

        if count <= 1:
            return head

        # Dummy head node.
        OneBefore = ListNode(0)
        OneBefore.next = head

        begin = head
        for i in range(m-1):
            if i == m - 2:
                OneBefore = begin 
            begin = begin.next

        prev = begin
        cur = begin.next
        for i in range(n - m):
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next

        End = prev
        OneAfter = cur

        OneBefore.next = End
        begin.next = cur

        if m == 1:
            return OneBefore.next
        else:
            return head
