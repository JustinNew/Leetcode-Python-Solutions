# 543. Diameter of Binary Tree
# Facebook Tag

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        if not root.left and not root.right:
            return 0

        l = self.depth(root.left)
        r = self.depth(root.right)

        d = l + r

        d_l = self.diameterOfBinaryTree(root.left)
        d_r = self.diameterOfBinaryTree(root.right)

        t = max(d_l, d_r)
        
        return max(d, t)            

    def depth(self, root):

        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left:
            return 1 + self.depth(root.right)
        elif not root.right:
            return 1 + self.depth(root.left)
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1
