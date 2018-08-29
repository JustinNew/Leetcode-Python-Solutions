# 382. Linked List Random Node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """

        self.head = head        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import numpy as np

        cur = self.head
        result = cur.val
        count = 1
        cur = cur.next
        while cur:
            count += 1
            if np.random.randint(0, count) == 0:
                result = cur.val
            cur = cur.next

        return result 

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
