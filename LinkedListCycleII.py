# 141. Linked List Cycle

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

        if not head:
            return False

        slow = head
        fast = head

        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

######################################################################################################################
# 142. Linked List Cycle II

'''
Tricky: check slow.next, fast.next and fast.next.next is not None.
First slow and fast, then two pointers one from head and the other from meet point.
'''

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        slow = head
        fast = head

        flag = 0
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                flag = 1
                break

        if flag == 1:
            p1 = head
            p2 = slow
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1
        else:
            return None
