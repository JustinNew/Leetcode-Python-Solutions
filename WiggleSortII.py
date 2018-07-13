# 324. Wiggle Sort II

# O(nlogn): quick sort and then half half insert.
# [1,2,3,4,5,6,7]
# [1,5,2,6,3,7,4]

# 1. Sort
# 2. First half and second half
# 3. Merge the two lists
# Note: nor O(n) time + O(1) space

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
