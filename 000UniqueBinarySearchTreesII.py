# 95. Unique Binary Search Trees II

# Extend of 96. Unique Binary Search Trees 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        nums = [i for i in range(1, n + 1)]

        return self.util(nums)

    def util(self, nums):

        if len(nums) == 0:
            return [None]

        if len(nums) == 1:
            n = TreeNode(nums[0])
            return [n]

        # result = [treenode1, treenode2, ...]
        result = []
        for i in range(len(nums)):
            left = self.util(nums[:i])
            right = self.util(nums[i + 1:])
            for i_l in left:
                for i_r in right:
                    n = TreeNode(nums[i])
                    n.left = i_l
                    n.right = i_r
                    result.append(n)

        return result
            
