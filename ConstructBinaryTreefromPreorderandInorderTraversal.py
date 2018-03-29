# 105. Construct Binary Tree from Preorder and Inorder Traversal

# Draw on paper how I will build a binary tree.
# 1. Use the first element in preorder list.
# 2. Break preorder and inorder lists into two lists.
# 3. Recursively build left and right nodes.
# Form solution based on that.
# Use recursion.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return None

        if len(preorder) == 1:
            n = TreeNode(preorder[0])
            return n

        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                index = i
                break

        n = TreeNode(preorder[0])
        n.left = self.buildTree(preorder[1:1 + index] , inorder[:index])
        n.right = self.buildTree(preorder[1 + index:] , inorder[index + 1:])

        return n       
