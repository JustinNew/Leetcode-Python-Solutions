# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        aux = []
        aux = self.util(root)

        return aux[k - 1]

    def util(self, root):

        if not root:
            return []

        return self.util(root.left) + [root.val] + self.util(root.right)
