# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque        

        result = []

        if root == None:
            return result

        dq = []
 
        dq.append(root)
        while dq:
            t = dq.pop()
            result.append(t.val)
            if t.right:
                dq.append(t.right)
            if t.left:
                dq.append(t.left)

        return result
