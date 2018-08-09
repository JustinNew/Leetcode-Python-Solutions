# 108. Convert Sorted Array to Binary Search Tree

# Select the middle, create root then create left and right.
# For left and right, they are done recursively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if len(nums) == 0:
            return None

        l = len(nums)
        mid = int(l / 2)

        n = TreeNode(nums[mid])
        n.left = self.sortedArrayToBST(nums[:mid])
        n.right = self.sortedArrayToBST(nums[mid+1:])

        return n
