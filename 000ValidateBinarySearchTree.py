# 98. Validate Binary Search Tree

# Use recursion. 
# Pass down two parameters: ceiling (which means that all nodes in the the current subtree must be smaller than this value) 
# and floor (all must be larger than it). 
# Compare root of the current subtree with these two values. 
# Then, recursively check the left and right subtree of the current one. 
# Take care of the values passed down.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def util(root, upperLimit, lowerLimit):

            if not root:
                return True

            if root.val >= upperLimit or root.val <= lowerLimit:
                return False

            return util(root.left, root.val, lowerLimit) and util(root.right, upperLimit, root.val)

        return util(root, float('inf'), float('-inf'))

# Based on InorderTraversal.

class Solution2:
    # @param root, a tree node
    # @return a boolean

    def isValidBST(self, root):
        output = []
        self.inOrder(root, output)
        
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False

        return True

    def inOrder(self, root, output):
        if root is None:
            return
        
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
