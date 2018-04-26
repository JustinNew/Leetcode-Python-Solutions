# 162. Find Peak Element

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        m = nums[0]

        for i in range(1, len(nums)):
            if i < len(nums) - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
            if nums[i] > m:
                m = nums[i]

        if m == nums[0]:
            return 0
        elif m == nums[-1]:
            return len(nums) - 1
