# 124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Do all possible searches.
    # Up or not.
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def getMax(root):
            
            if not root:
                return [float('-inf'), float('-inf')]

            (left_up, left_stop) = getMax(root.left)
            (right_up, right_stop) = getMax(root.right)

            up_max = max(root.val, root.val + left_up, root.val + right_up)
            stop_max = max(left_up + right_up + root.val, left_stop, right_stop, left_up, right_up)

            return [up_max, stop_max]
        
        return max(getMax(root))

    # Exactly same idea but fast code.
    def maxPathSum(self, root):

        def maxsums(node):
            if not node:
                return [-2**31] * 2
            left = maxsums(node.left)
            right = maxsums(node.right)
            return [node.val + max(left[0], right[0], 0),
                    max(left + right + [node.val + left[0] + right[0]])]

    return max(maxsums(root))
