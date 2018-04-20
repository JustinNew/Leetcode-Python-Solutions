# 147. Insertion Sort List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    # Time Limit Exceeded.
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cur = head.next
        head.next = None

        while cur:
            next = cur.next

            if cur.val < dummy.next.val:
                dummy.next = cur
                cur.next = head
                head = dummy.next
            else:
                in_cur = head
                while in_cur.next:
                    in_next = in_cur.next
                    if cur.val >= in_cur.val and cur.val < in_next.val:
                        in_cur.next = cur
                        cur.next = in_next
                        break
                    in_cur = in_next

                if not in_cur.next:
                    in_cur.next = cur
                    cur.next = None

            cur = next

        return dummy.next

    # Only Move the Ones that need to be moved.
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = head
        cur = head.next
 
        while cur:
            next = cur.next
            if cur.val >= prev.val:
                prev = cur
                cur = next
            else:
                prev.next = next
                in_prev = dummy
                in_cur = dummy.next
                while in_cur != next:
                    if cur.val < in_cur.val:
                        in_prev.next = cur
                        cur.next = in_cur
                        cur = next
                        break
                    else:
                        in_prev = in_cur
                        in_cur = in_cur.next
                
        return dummy.next
