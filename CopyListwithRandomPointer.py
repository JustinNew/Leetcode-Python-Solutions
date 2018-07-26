# 138. Copy List with Random Pointer

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if not head:
            return None

        toCopyNodes = []
        CopiedNodes = []
        dummy = RandomListNode(0)
        head_copied = dummy

        toCopyNodes.append(head)
        n = RandomListNode(head.label)
        CopiedNodes.append(n)
        dummy.next = n
        dummy = dummy.next

        while head:

            if head.next and head.next not in toCopyNodes:
                toCopyNodes.append(head.next)
                n_next = RandomListNode(head.next.label)
                CopiedNodes.append(n_next)
                dummy.next = n_next
            elif head.next:
                i = toCopyNodes.index(head.next)
                dummy.next = CopiedNodes[i]

            if head.random and head.random not in toCopyNodes:
                toCopyNodes.append(head.random)
                n_random = RandomListNode(head.random.label)
                CopiedNodes.append(n_random)
                dummy.random = n_random
            elif head.random:
                i = toCopyNodes.index(head.random)
                dummy.random = CopiedNodes[i]

            head = head.next
            dummy = dummy.next

        return head_copied.next
