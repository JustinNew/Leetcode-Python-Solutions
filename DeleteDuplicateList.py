# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None
        elif head and not head.next:
            return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            previous = dummy
            
            current = head
            next = current.next
            flag = 0
            while next:
                if next.val == current.val:
                    flag = 1
                else:
                    if flag == 0:
                        previous = current
                        current = next
                    else:
                        previous.next = next
                        current = next
                        flag = 0
                next = next.next
        
        if flag == 1:
            previous.next = None
         
        return dummy.next           
