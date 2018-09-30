# 138. Copy List with Random Pointer

'''
Similar to copy linked list.
Need to have two lists to record the nodes of the original and the copied nodes in order as we copy the list.
'''


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

        origin = []
        copied = []

        copy = RandomListNode(head.label)
        res = copy

        origin.append(head)
        copied.append(copy)

        while head:
            next = head.next
            random = head.random

            if next in origin:
                i = origin.index(next)
                copy.next = copied[i]
            elif next:
                copy.next = RandomListNode(next.label)
                origin.append(next)
                copied.append(copy.next)

            if random in origin:
                i = origin.index(random)
                copy.random = copied[i]
            elif random:
                copy.random = RandomListNode(random.label)
                origin.append(random)
                copied.append(copy.random)

            head = next
            copy = copy.next

        return res
