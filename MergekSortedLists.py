# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        while True:

            temp = []
            while len(lists) > 1:
                l1 = lists.pop()
                l2 = lists.pop()
                temp.append(self.merge2(l1, l2))

            if lists:
                temp.append(lists.pop())

            if len(temp) == 1:
                return temp[0]

            lists = temp
            
    def merge2(self, list1, list2):

        if not list1:
            return list2

        if not list2:
            return list1

        dummy = ListNode(0)
        head = dummy

        while list1 and list2:

            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        if not list1:
            head.next = list2

        if not list2:
            head.next = list1

        return dummy.next
