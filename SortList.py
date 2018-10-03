# 148. Sort List

# Merge Sort:
# Divide and Conquer
# Solve it recursively. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return head

        cur = head
        count = 0
        while cur:
           count += 1
           cur = cur.next

        # Divide
        l = int(count / 2)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        right = head
        for i in range(l):
            prev = prev.next
            right = right.next
        prev.next = None

        # Conquer
        left = self.sortList(head)
        right = self.sortList(right)
         
        # Merge
        head = self.Merge(left, right)

        return head

    def Merge(self, left, right):

        if not left and not right:
            return None
        elif not left:
            return right
        elif not right:
            return left
   
        dummy = ListNode(0)
        head = dummy

        while left and right:
            l_next = left.next
            r_next = right.next

            if left.val < right.val:
                head.next = left
                head = head.next
                left.next = None
                left = l_next
            else:
                head.next = right
                head = head.next
                right.next = None
                right = r_next

        if left:
            head.next = left
        elif right:
            head.next = right

        return dummy.next

###############################################################################################################################
# All in one function.

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next

        if count == 1:
            return head
        else:
            half = int(count / 2)
            left_head = ListNode(0)
            left = left_head
            left.next = head
            while half > 0:
                left = left.next
                half -= 1

            right_head = ListNode(0)
            right = right_head
            right.next = left.next

            left.next = None

            left_head.next = self.sortList(left_head.next)
            right_head.next = self.sortList(right_head.next)

            all_head = ListNode(0)
            all = all_head
            left = left_head.next
            right = right_head.next

            while left and right:
                if left.val < right.val:
                    all.next = left
                    n = left.next
                    left.next = None
                    left = n
                else:
                    all.next = right
                    n = right.next
                    right.next = None
                    right = n
                all = all.next

            if left:
                all.next = left
            else:
                all.next = right

            return all_head.next 
