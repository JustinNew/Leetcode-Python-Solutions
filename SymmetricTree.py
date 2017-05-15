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
        from collections import deque

        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):

        if left==None and right== None:
            return True
        elif left==None or right==None:
            return False

        if left.val==right.val:
            outPair = self.isMirror(left.left, right.right)
            innerPair = self.isMirror(left.right, right.left)
            return outPair and innerPair
        else:
            return False

