# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        result = []
        temp = []

        self.util(root, sum, temp, result)

        return result

    def util(self, root, sum, temp, result):

        t = 0
        for i in temp:
            t += i

        if not root:
            return

        if not root.left and not root.right and t + root.val == sum:
            result.append(temp+[root.val])
            return
        else:
            self.util(root.left, sum, temp+[root.val], result)
            self.util(root.right, sum, temp+[root.val], result)
