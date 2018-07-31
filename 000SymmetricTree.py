# 101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True

        def isMirror(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)
