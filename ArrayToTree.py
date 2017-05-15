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
        if len(nums)==0:
            return None
        elif len(nums)==1:
            return TreeNode(nums[0])
        else:

            mid = len(nums)//2

            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[0:mid])
            root.right = sortedArrayToBST(nums[mid+1:len(nums)])

            return root
