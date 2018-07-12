# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Need to do all possible searches.

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def util(root):
            if not root:
                return [float('-inf'), float('-inf')]
            if not root.left and not root.right:
                return [root.val, root.val]

            left = util(root.left)
            right = util(root.right)

            up_max = max(root.val, root.val + left[0], root.val + right[0])
            stop_max = max(left[1], right[1], root.val + left[0] + right[0], left[0], right[0])

            print (up_max, stop_max)
            return [up_max, stop_max]

        result = util(root)

        return max(result)
