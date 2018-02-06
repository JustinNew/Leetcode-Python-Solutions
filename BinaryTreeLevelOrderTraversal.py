# 102. Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []
        nodes = []

        if root:
            nodes.append(root)
        else:
            return result

        while True:
            
            tempNodes = []
            tempR = []
            for i in range(len(nodes)):
                s = nodes[i]
                tempR.append(s.val)
                if s.left:
                    tempNodes.append(s.left)
                if s.right:
                    tempNodes.append(s.right)

            result.append(tempR)
            nodes = tempNodes
            
            if len(tempNodes) == 0:
                return result
