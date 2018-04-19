# 143. Reorder List

# Be careful about trailing pointers. 
# 1. Count
# 2. Divide
# 3. Reverse second half
# 4. Merge to list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """

        if not head:
            return

        cur = head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        second = head

        for i in range(int(count / 2)):
            second = second.next

        next = second.next
        second.next = None

        second = self.reverseList(next)

        while head and second:
            next = head.next
            second_next = second.next

            head.next = second
            second.next = next

            head = next
            second = second_next
           
        return

    def reverseList(self, head):

        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = dummy.next

        while cur.next:
            next = cur.next
            cur.next = prev
            
            prev = cur
            cur = next

        cur.next = prev
        head.next = None

        return cur 
