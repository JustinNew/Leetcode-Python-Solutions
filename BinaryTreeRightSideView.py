# 199. Binary Tree Right Side View

# Level traveral and save the last element for each level.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        s = []
        s.append(root)
        result = []

        while True:

            temp = []
            for n in s:
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)

            result.append(n.val)
            if len(temp) != 0:
                s = temp
            else:
                return result
