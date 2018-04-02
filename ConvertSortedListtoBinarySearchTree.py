# 109. Convert Sorted List to Binary Search Tree

# Solve it recursively.
# Find the middle one and divide into left and right linked lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # Count number of Nodes.
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        # Special Cases.
        if count == 0:
            return None
        if count == 1:
            n = TreeNode(head.val)
            return n

        # Split the linked list.
        current = head
        for i in range(int(count/2)):
            previous = current
            current = current.next

        right = current.next
        left = head
        previous.next = None

        # Build the BST recursively.
        n = TreeNode(current.val)
        n.left = self.sortedListToBST(left)
        n.right = self.sortedListToBST(right)

        return n
