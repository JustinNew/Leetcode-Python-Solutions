# Code for the merge subroutine

def MergeSort(nums):

    if len(nums) <= 1:
        return nums

    l = len(nums)
    mid = int(l / 2)

    left = MergeSort(nums[:mid])
    right = MergeSort(nums[mid:])

    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i == len(left):
        for k in range(j, len(right)):
            result.append(right[k])
    elif j == len(right):
        for k in range(i, len(left)):
            result.append(left[k])

    return result

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
