# Code for the merge subroutine

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

# Code for merge sort

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

###################################################################
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
